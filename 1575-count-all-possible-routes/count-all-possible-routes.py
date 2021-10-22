class Solution:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:
        result = 0
        cache = [[-1 for _ in range(201)] for _ in range(101)]
        dest = finish

        @functools.lru_cache(None)
        def recurSol(cur: int, fuel: int) -> int:
            ret = 0
            if (cur == dest):
                ret += 1

            for i in range(len(locations)):
                if (i != cur):
                    newFuel = fuel - abs(locations[i] - locations[cur])
                    if (newFuel >= 0):
                        ret += recurSol(i, newFuel)
            return ret
        
        return recurSol(start, fuel) % (10**9 + 7)
    
s = Solution() 
print(s.countRoutes([2, 3, 6, 8, 4], 1, 3, 5))

s = Solution() 
print(s.countRoutes([4, 3, 1], 1, 0, 6))

s = Solution() 
print(s.countRoutes([5, 2, 1], 0, 2, 3))

s = Solution() 
print(s.countRoutes([2, 1, 5], 0, 0, 3))

s = Solution() 
print(s.countRoutes([1, 2, 3], 0, 2, 40))

l = [1528,1529,1530,1531,1532,1533,1534,1535,1536,1538,1539,1540,1541,1542,1543,1544,1545,1546,1547,1548,1549,1550,1551,1552,1553,1554,1555,1556,1557,1558,1559,1560,1561,1562,1563,1564,1565,1566,1567,1568,1569,1570,1571,1572,1573,1574,1575,1576,1577,1578,1579,1580,1581,1582,1583,1584,1585,1586,1587,1588,1589,1590,1591,1592,1593,1594,1595,1596,1597,1598,1599,1600,1601,1602,1603,1604,1605,1606,1607,1608,1609,1610,1611,1612,1613,1614,1615,1616,1617,1618,1619,1620,1621,1622,1623,1624,1625,1626,1627,1628]
s = Solution() 
print(s.countRoutes(l, 50, 50, 200))