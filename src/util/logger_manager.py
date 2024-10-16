"""Modulo per la gestione dei log dell'applicazione."""

# Standard Import
import logging

# Site-package Import
# Project Import


class LoggerManager:
    ''' Creo la classe Logger per creare un logger separato per ogni modulo.
        Occorre passare il nome del modulo e l'eventuale nomefile.
        Se non viene passato un nomefile, si utiizza lo standard.

        NOTSET     0  Non impostato
        DEBUG     10  Livello di Debug
        INFO      20  Livello di Informazione da mettere in output
        WARNING   30  Warning non bloccante
        ERROR     40  Errore
        CRITICAL  50  Errore critico bloccante
    '''

    ''' PARAMETRI:
        name              Nome che si vuole assegnare al logger
        log_file          Nome_file per outpu su file. None=non viene creato 
        base_log_level    Livello base del logger
        file_log_level    Livello di log per l'output su File
        console_log_level Livello di log per l'outpu su consolle 
    '''

    def __init__(self, name, log_file=None,
                 base_log_level=1, file_log_level=None, console_log_level=None):
        
        self.logger = logging.getLogger(name)
        
        # Verifica livello BASE del Debug: standard = 1: passa tutto
        base_log_level = min(max(base_log_level, 0), 50) if isinstance(base_log_level, int) else 1

        # Verifica livello Debug per File: standard = 20: INFO
        file_log_level = min(max(file_log_level, 0), 50) if isinstance(file_log_level, int) else 20
        
        # Verifica livello Log per Console: standard = 10: DEBUG
        console_log_level = min(max(console_log_level, 0), 50) if isinstance(console_log_level, int) else 10
              
        # Imposto il livello alla base dei log che vengono passati agli Handler
        self.logger.setLevel(base_log_level)

        # imposto i 2 formatter per il File (DateTime) e per la Consolle (no DateTime)
        file_formatter = logging.Formatter("%(asctime)s %(name)s > %(levelname)-9s%(message)s", datefmt="%Y.%m.%d %H:%M:%S")
        cons_formatter = logging.Formatter("%(name)s > %(levelname)-9s%(message)s")    

        if log_file:
            ''' se viene passato un log_file creo l'Handler altrimenti solo su console'''
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(file_log_level)
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)
        
        ''' sulla Console imposto sempre il Logging, poi valutiamo insieme'''
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_log_level)
        console_handler.setFormatter(cons_formatter)
        self.logger.addHandler(console_handler)

if(__name__ == "__main__"):
    logger_manager = LoggerManager(__name__, file_log_level=30, console_log_level=10)
    logger = logger_manager.logger
    logger.debug('test con un "Debug level"')
    logger.info('test con un "Info level"')
    logger.warning('test con un "Warning level"')
    logger.error('test con un "ERROR level !!!!"')
    logger.critical('test con un "CRITICAL level !!!!"')


''' 
Rimangono da gestire:
- i file per data o altro metodo (dimensione ?)
- il progressivo all'interno della stessa data (o mettiamo da Ora a Ora)
- verifica del superamento di una soglia di dimensione per i file su disco
- 
'''

