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

type head struct {
	x int
	y int
}
type point struct {
	x int
	y int
}

type link struct {
	hd *head
	pt *point
}

func main() {
	inst, err := read("input1.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	//fmt.Println(inst)
	visited := position(inst, 10)
	fmt.Println(visited)

}

func position(tab_ins []instructs, num_point int) int {
	h := head{x: 0, y: 0}
	var l link
	for i := 0; i < num_point; i++ {
		l.hd = &h
		l.pt = &point{x: 0, y: 0}
		h = head(*l.pt)
	}

	p := point{x: 0, y: 0}
	var tab_pos []point
	for _, ins := range tab_ins {
		for i := 0; i < ins.rep; i++ {
			calcul_head_pos(ins, &h)
			calcul_tail_pos(&h, &p)
			calcul_is_visited(&tab_pos, &p)
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

func calcul_tail_pos(h *head, p *point) {
	//xa = t.x	xb = h.x
	//ya = t.y	yb = h.y
	x := h.x - p.x
	y := h.y - p.y

	if x > 1 {
		p.x += 1
		p.y += y
	}
	if y > 1 {
		p.y += 1
		p.x += x
	}
	if x < -1 {
		p.x += -1
		p.y += y
	}
	if y < -1 {
		p.y += -1
		p.x += x
	}

}

func calcul_head_pos(ins instructs, h *head) {
	switch {
	case ins.direction == "R":
		h.x += 1
	case ins.direction == "L":
		h.x -= 1
	case ins.direction == "U":
		h.y += 1
	case ins.direction == "D":
		h.y -= 1
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
