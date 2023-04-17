from ekumenlabs_config import get_string_config
from ekumenlabs_config.exceptions import ConfigurationError
from ekumenlabs_config.models import ConfigValue
from tests import BasicTestCase


class StringConfigTestCase(BasicTestCase):
    async def test_simple_config(self):
        await ConfigValue.create_string("simple.key", "AA")
        self.assertEqual(await ConfigValue.get_string("simple.key"), "AA")

    async def test_syntactic_sugar(self):
        await ConfigValue.create_string("simple.key", "BB")
        self.assertEqual(await get_string_config("simple.key"), "BB")

    async def test_non_existent_key(self):
        with self.assertRaises(ConfigurationError):
            await ConfigValue.get_string("simple.key")

    async def test_wrong_type(self):
        await ConfigValue.create_bool("simple.key", True)
        with self.assertRaises(ConfigurationError):
            await ConfigValue.get_string("simple.key")

    async def test_invalid_create(self):
        with self.assertRaises(ValueError):
            await ConfigValue.create_string("simple.key", 1)
        with self.assertRaises(ValueError):
            await ConfigValue.create_string("simple.key", True)
