from ekumenlabs_config import get_bool_config
from ekumenlabs_config.exceptions import ConfigurationError
from ekumenlabs_config.models import ConfigValue
from tests import BasicTestCase


class BoolConfigTestCase(BasicTestCase):
    async def test_simple_config(self):
        await ConfigValue.create_bool("simple.key", True)
        self.assertTrue(await ConfigValue.get_boolean("simple.key"))

    async def test_syntactic_sugar(self):
        await ConfigValue.create_bool("simple.key", False)
        self.assertFalse(await get_bool_config("simple.key"))

    async def test_non_existent_key(self):
        with self.assertRaises(ConfigurationError):
            await ConfigValue.get_boolean("simple.key")

    async def test_wrong_type(self):
        await ConfigValue.create_string("simple.key", "True")
        with self.assertRaises(ConfigurationError):
            await ConfigValue.get_boolean("simple.key")

    async def test_invalid_create(self):
        with self.assertRaises(ValueError) as e:
            await ConfigValue.create_bool("simple.key", 1)
        self.assertEqual(str(e.exception), "Value >1< is not a bool")

        with self.assertRaises(ValueError):
            await ConfigValue.create_bool("simple.key", "AA")
