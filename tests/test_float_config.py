from ekumenlabs_config import get_float_config
from ekumenlabs_config.exceptions import ConfigurationError
from ekumenlabs_config.models import ConfigValue
from tests import BasicTestCase


class FloatConfigTestCase(BasicTestCase):
    async def test_simple_config(self):
        await ConfigValue.create_float("simple.key", 1.4)
        self.assertEqual(await ConfigValue.get_float("simple.key"), 1.4)

    async def test_syntactic_sugar(self):
        await ConfigValue.create_float("simple.key", 1.5)
        self.assertEqual(await get_float_config("simple.key"), 1.5)

    async def test_non_existent_key(self):
        with self.assertRaises(ConfigurationError):
            await ConfigValue.get_int("simple.key")

    async def test_wrong_type(self):
        await ConfigValue.create_string("simple.key", "True")
        with self.assertRaises(ConfigurationError):
            await ConfigValue.get_float("simple.key")

    async def test_invalid_create(self):
        with self.assertRaises(ValueError):
            await ConfigValue.create_float("simple.key", True)
        with self.assertRaises(ValueError):
            await ConfigValue.create_float("simple.key", "AA")
