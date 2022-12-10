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
	inst, err := read("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(inst)
	position(inst)

}

func position(tab_ins []instructs) {
	h := head{x: 0, y: 0}
	t := tail{x: 0, y: 0}
	for _, ins := range tab_ins {
		for i := 0; i < ins.rep; i++ {
			calcul_head_pos(ins, &h)
			calcul_tail_pos(&h, &t)
		}
	}
}

func calcul_tail_pos(h *head, t *tail) {
	//xa = t.x	xb = h.x
	//ya = t.y	yb = h.y
	x := h.x - t.x
	y := h.y - t.y

	if x >= 1 {
		t.x += x
	}
	if y >= 1 {
		t.y += y
	}
	if x <= -1 {
		t.x += x
	}
	if y <= -1 {
		t.y += y
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
