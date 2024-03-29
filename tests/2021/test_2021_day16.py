import aoc_cas.aoc2021.day16 as aoc


def testPartA():
    assert aoc.part_a("8A004A801A8002F478") == 16
    assert aoc.part_a("620080001611562C8802118E34") == 12
    assert aoc.part_a("C0015000016115A2E0802F182340") == 23
    assert aoc.part_a("A0016C880162017C3686B18A3D4780") == 31


def testPartB():
    assert aoc.part_b("C200B40A82") == 3
    assert aoc.part_b("880086C3E88112") == 7
    assert aoc.part_b("CE00C43D881120") == 9
    assert aoc.part_b("D8005AC2A8F0") == 1
    assert aoc.part_b("F600BC2D8F") == 0
    assert aoc.part_b("9C005AC2F8F0") == 0
    assert aoc.part_b("9C0141080250320F1802104A08") == 1
