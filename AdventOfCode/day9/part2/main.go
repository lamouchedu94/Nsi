package main

import (
	"bufio"
	"fmt"
	"os"
)

type instructs struct {
	direction string
	rep       int
}

type point struct {
	x int
	y int
}

type rope []point

func main() {
	inst, err := read("../input1.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	//fmt.Println(inst)
	visited := position(inst, 10)
	fmt.Println(visited)

}

func position(tab_ins []instructs, nb_point int) int {
	rope := make(rope, nb_point)

	var tab_pos []point
	for _, ins := range tab_ins {
		for i := 0; i < ins.rep; i++ {
			calcul_head_pos(ins, &rope[0])
			for j := 1; j < nb_point; j++ {
				calcul_tail_pos(&rope[j-1], &rope[j])
			}
			calcul_is_visited(&tab_pos, &rope[nb_point-1])

		}
	}
	return len(tab_pos)
}

func calcul_is_visited(tab_pos *[]point, p *point) {
	for _, pos := range *tab_pos {
		if pos.x == p.x && pos.y == p.y {
			return
		}
	}
	*tab_pos = append(*tab_pos, *p)
}

func calcul_tail_pos(h *point, p *point) {
	//xa = t.dx	xb = h.dx
	//ya = t.y	yb = h.y
	dx := h.x - p.x
	dy := h.y - p.y

	switch {
	case abs(dx) > 1 && dy == 0:
		p.x += signe(dx)

	case abs(dy) > 1 && dx == 0:
		p.y += signe(dy)

	case abs(dx) > 1 || abs(dy) > 1:
		p.x += signe(dx)
		p.y += signe(dy)
	}
}

func signe(num int) int {
	if num == 0 {
		return 0
	}
	if num > 0 {
		return 1
	}
	return -1
}

func abs(num int) int {
	if num > 0 {
		return num
	}
	return -num
}

func calcul_head_pos(ins instructs, p *point) {
	switch {
	case ins.direction == "R":
		p.x += 1
	case ins.direction == "L":
		p.x -= 1
	case ins.direction == "U":
		p.y += 1
	case ins.direction == "D":
		p.y -= 1
	}

}

func read(path string) ([]instructs, error) {
	var tab []instructs
	file, err := os.Open(path)
	if err != nil {
		file.Close()
		return nil, err
	}

	defer file.Close()
	test := bufio.NewScanner(file)
	test.Split(bufio.ScanLines)

	for test.Scan() {
		var ins instructs
		fmt.Sscanf(test.Text(), "%s %d", &ins.direction, &ins.rep)
		tab = append(tab, ins)
	}
	return tab, err

}
