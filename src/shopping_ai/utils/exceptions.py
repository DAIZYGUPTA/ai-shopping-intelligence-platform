class ShoppingAIException(Exception):
    """
    Base exception for the project.
    """

    pass


class BrowserInitializationError(
    ShoppingAIException
):
    pass


class ProductDiscoveryError(
    ShoppingAIException
):
    pass


class ProductScrapingError(
    ShoppingAIException
):
    pass


class ReviewScrapingError(
    ShoppingAIException
):
    pass


class AnalysisError(
    ShoppingAIException
):
    pass