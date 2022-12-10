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
type tail struct {
	x int
	y int
}

func main() {
	inst, err := read("input1.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	//fmt.Println(inst)
	visited := position(inst)
	fmt.Println(visited)

}

func position(tab_ins []instructs) int {
	h := head{x: 0, y: 0}
	t := tail{x: 0, y: 0}
	var tab_pos []tail
	for _, ins := range tab_ins {
		for i := 0; i < ins.rep; i++ {
			calcul_head_pos(ins, &h)
			calcul_tail_pos(&h, &t)
			calcul_is_visited(&tab_pos, &t)
		}
	}
	return len(tab_pos)
}

func calcul_is_visited(tab_pos *[]tail, t *tail) {
	for _, pos := range *tab_pos {
		if pos.x == t.x && pos.y == t.y {
			return
		}
	}
	*tab_pos = append(*tab_pos, *t)
}

func calcul_tail_pos(h *head, t *tail) {
	//xa = t.x	xb = h.x
	//ya = t.y	yb = h.y
	x := h.x - t.x
	y := h.y - t.y

	if x > 1 {
		t.x += 1
		t.y += y
	}
	if y > 1 {
		t.y += 1
		t.x += x
	}
	if x < -1 {
		t.x += -1
		t.y += y
	}
	if y < -1 {
		t.y += -1
		t.x += x
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
