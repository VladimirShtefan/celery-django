import requests
from celery import shared_task
from celery.utils.log import get_task_logger

from config import RATES_API_URL
from coverter.models import Rate
from coverter.serializers import RateSerializer

logger = get_task_logger(__name__)


@shared_task
def sample_task() -> None:
    """

    :return:
    """
    api_data = get_rates_api()
    converted_data = covert_info(api_data)
    serializer = RateSerializer(data=converted_data, many=True)
    if serializer.is_valid():
        serializer.save()
    else:
        logger.info("Bad data from rates API")


def get_rates_api() -> dict:
    """

    :return:
    """
    return requests.get(
        RATES_API_URL,
        params={
            "app_id": "e5e897ff7a85439eba43e2e1c4803bb4"
        }
    ).json()


def covert_info(data: dict) -> list[dict]:
    """

    :param data:
    :return:
    """
    return [
        {
            "short_name": key,
            "rate_to_usd": value,
        }
        for key, value in data["rates"].items()
        if key in Rate.Name.values
    ]
