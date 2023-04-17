from ekumenlabs_config import get_int_config
from ekumenlabs_config.exceptions import ConfigurationError
from ekumenlabs_config.models import ConfigValue
from tests import BasicTestCase


class IntConfigTestCase(BasicTestCase):
    async def test_simple_config(self):
        await ConfigValue.create_integer("simple.key", 1)
        self.assertEqual(await ConfigValue.get_int("simple.key"), 1)

    async def test_syntactic_sugar(self):
        await ConfigValue.create_integer("simple.key", 2)
        self.assertEqual(await get_int_config("simple.key"), 2)

    async def test_non_existent_key(self):
        with self.assertRaises(ConfigurationError):
            await ConfigValue.get_int("simple.key")

    async def test_wrong_type(self):
        await ConfigValue.create_string("simple.key", "1")
        with self.assertRaises(ConfigurationError):
            await ConfigValue.get_int("simple.key")

    async def test_invalid_create(self):
        with self.assertRaises(ValueError):
            await ConfigValue.create_integer("simple.key", True)
        with self.assertRaises(ValueError):
            await ConfigValue.create_integer("simple.key", "AA")
