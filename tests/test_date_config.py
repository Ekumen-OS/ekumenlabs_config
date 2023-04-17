from datetime import date

from ekumenlabs_config import get_date_config
from ekumenlabs_config.exceptions import ConfigurationError
from ekumenlabs_config.models import ConfigValue
from tests import BasicTestCase


class DateConfigTestCase(BasicTestCase):
    async def test_simple_config(self):
        today = date.today()
        await ConfigValue.create_date("simple.key", today)
        self.assertEqual(await ConfigValue.get_date("simple.key"), today)

    async def test_syntactic_sugar(self):
        today = date.today()
        await ConfigValue.create_date("simple.key", today)
        self.assertEqual(await get_date_config("simple.key"), today)

    async def test_non_existent_key(self):
        with self.assertRaises(ConfigurationError):
            await ConfigValue.get_date("simple.key")

    async def test_wrong_type(self):
        await ConfigValue.create_bool("simple.key", True)
        with self.assertRaises(ConfigurationError):
            await ConfigValue.get_date("simple.key")

    async def test_invalid_create(self):
        with self.assertRaises(ValueError):
            await ConfigValue.create_date("simple.key", 1)
        with self.assertRaises(ValueError):
            await ConfigValue.create_date("simple.key", True)
