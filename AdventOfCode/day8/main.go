package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type tree struct {
	line   int
	colone int
	height int
}

type forest struct {
	tree   []tree
	line   int
	colone int
}

func main() {
	tab, foret, err := read("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	print(tab)
	//fmt.Println(foret.tree)
	//fmt.Println(foret.line, foret.colone)
	fmt.Println(visible(foret))
}

func calc_vis(f forest, t tree) bool {
	var horizontal bool = false
	var vertical bool = false
	//top
	for _, li := range f.tree {
		if t.line == li.line && t.colone != li.colone {
			if li.height < t.height {
				horizontal = true
			} else {
				break
			}
		}
	}
	//left
	for _, cl := range f.tree {
		if t.colone == cl.colone && t.line != cl.line {
			if cl.height < t.height {
				vertical = true
			} else {
				break
			}
		}
	}

	return horizontal || vertical
}

func visible(f forest) int {
	var vis int
	for _, obj := range f.tree {
		switch {
		case obj.line == 0 || obj.line == f.line:
			vis += 1
		case obj.colone == 0 || obj.colone == f.colone:
			vis += 1
		default:
			if calc_vis(f, obj) {
				vis += 1
			}
		}

	}

	return vis
}

func print(tab []string) {
	for _, line := range tab {
		fmt.Println(line)
	}
}

func read(path string) ([]string, forest, error) {
	var tab []string
	file, err := os.Open(path)
	if err != nil {
		return nil, forest{}, err
	}
	defer file.Close()
	test := bufio.NewScanner(file)
	test.Split(bufio.ScanLines)
	var f forest
	var ligne int
	var col int
	for test.Scan() {
		for i, arbre := range test.Text() {
			temp, _ := strconv.Atoi(string(arbre))
			t := tree{line: ligne, colone: i, height: temp}
			f.tree = append(f.tree, t)
			col = i
		}
		ligne += 1
		tab = append(tab, test.Text())
	}
	f.line = ligne - 1
	f.colone = col

	return tab, f, err

}
