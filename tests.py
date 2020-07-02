import unittest
import pprint

from gear_torque_calc import get_torque

pp = pprint.PrettyPrinter()


class TorqueTests(unittest.TestCase):
    def test_stock(self):
        res = get_torque(
            drive_shaft_diameter=5,
            drive_shaft_torque=0.2,
            gear_small_diameter=15,
            gear_large_diameter=55,
        )
        self.assertEqual(res["motor"]["force"], 80)
        self.assertAlmostEqual(res["small_gear"]["force"], 26.6667, places=4)
        self.assertAlmostEqual(res["small_gear"]["torque"], 0.2, places=4)
        self.assertAlmostEqual(res["large_gear"]["force"], 26.6667, places=4)
        self.assertAlmostEqual(res["large_gear"]["torque"], 0.733334, places=4)
        pp.pprint(res)

    def test_double_sprocket(self):
        res = get_torque(
            drive_shaft_diameter=5,
            drive_shaft_torque=0.2,
            gear_small_diameter=15,
            gear_large_diameter=55 * 2,
        )
        pp.pprint(res)


if __name__ == "__main__":
    unittest.main()
