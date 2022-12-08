package main

import (
	"bufio"
	"fmt"
	"os"
)

type forest struct {
	tout [][]byte
}

func main() {
	tab, err := read("input1.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	//print(tab)
	fmt.Println(visible(tab))
}

func calc_visible(f forest, v int, h int) bool {
	vis := true
	mon_arbre := f.tout[v][h]
	//left
	for i := 0; i < h; i++ {
		if f.tout[v][i] >= mon_arbre {
			vis = false
			break
		}
		//fmt.Println(string(f.tout[h][i]))
	}
	if vis {
		return vis
	}

	vis = true
	//right
	for i := h + 1; i < len(f.tout[0]); i++ {
		if f.tout[v][i] >= mon_arbre {
			vis = false
			break
		}
		//fmt.Println(string(f.tout[h][i]))
	}
	if vis {
		return vis
	}
	//top
	vis = true
	for i := 0; i < v; i++ {
		if f.tout[i][h] >= mon_arbre {
			vis = false
			break
		}
		//fmt.Println(string(f.tout[h][i]))
	}
	//bottom
	if vis {
		return vis
	}
	vis = true
	for i := v + 1; i < len(f.tout); i++ {
		if f.tout[i][h] >= mon_arbre {
			vis = false
			break
		}
		//fmt.Println(string(f.tout[h][i]))
	}
	if vis {
		return vis
	}

	return false
}

func visible(f forest) int {
	vis := 0
	for v := 0; v < len(f.tout); v++ {
		for h := 0; h < len(f.tout[0]); h++ {

			if v == 0 || h == 0 || v == len(f.tout)-1 || h == len(f.tout[0])-1 {
				vis += 1
				continue
			}

			if calc_visible(f, v, h) {

				vis += 1
			}

		}
	}
	return vis
}

func print(tab forest) {
	for _, t := range tab.tout {
		for _, line := range t {
			fmt.Print(string(line))
		}
		fmt.Println()
	}
}

func read(path string) (forest, error) {
	file, err := os.Open(path)
	if err != nil {
		return forest{}, err
	}
	defer file.Close()
	test := bufio.NewScanner(file)
	test.Split(bufio.ScanLines)
	var f forest
	for test.Scan() {
		row := make([]byte, len(test.Bytes()))
		copy(row, test.Bytes())
		f.tout = append(f.tout, row)
	}

	return f, err

}
