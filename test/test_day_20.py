import pytest
import day_20

inp = ["..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"]
pic = ["#..#.",
"#....",
"##..#",
"..#..",
"..###"]


def test_enhanceTwise():
    enhPic = day_20.extendPicture00(pic)
    enhPic = day_20.enhancePicture(enhPic, inp)
    enhPic = day_20.extendPicture00(enhPic)
    enhPic2 = day_20.enhancePicture(enhPic, inp)
    o  = day_20.countPixels(enhPic2)
    assert o == 35

def test_enhance50():
    epic = pic.copy()
    for i in range(50):
        epic = day_20.extendPicture00(epic)
        epic = day_20.enhancePicture(epic, inp)
    o  = day_20.countPixels(epic)
    assert o == 3351


# Run tests from terminal:
# $ pytest test/test_day_20.py s