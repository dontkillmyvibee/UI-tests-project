from enum import Enum


class AppRoute(str, Enum):
    MAIN_PAGE = './#practice-areas'
    AUTHENTICATION = './authentication'
    FORM_ELEMENTS = './forms'
    DYNAMIC_ELEMENTS = './dynamic-elements'
    TABLES = './tables'
    ALERTS_AND_MODALS = './alerts-modals'
    DRAG_AND_DROP = './drag-drop'
    IFRAMES = './iframes'
    ADVANCED_INTERACTIONS = './advanced-interactions'
