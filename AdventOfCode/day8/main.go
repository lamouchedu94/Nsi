package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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

func calc_visible(f forest, v int, h int) int {
	count := 1
	temp := 0
	mon_arbre := f.tout[v][h]
	//left
	for i := h - 1; i >= 0; i-- {
		temp += 1
		if f.tout[v][i] >= mon_arbre {
			break
		}
		//fmt.Println(string(f.tout[h][i]))
	}
	count *= temp

	//right
	temp = 0
	for i := h + 1; i < len(f.tout[0]); i++ {
		temp++
		if f.tout[v][i] >= mon_arbre {
			break
		}
		//fmt.Println(string(f.tout[h][i]))
	}
	count *= temp

	//top
	temp = 0
	for i := v - 1; i >= 0; i-- {
		temp += 1
		if f.tout[i][h] >= mon_arbre {
			break
		}
		//fmt.Println(string(f.tout[h][i]))
	}
	count *= temp

	//bottom
	temp = 0
	for i := v + 1; i < len(f.tout); i++ {
		temp += 1
		if f.tout[i][h] >= mon_arbre {
			break
		}
		//fmt.Println(string(f.tout[h][i]))
	}
	count *= temp
	return count
}

func visible(f forest) int {
	var res []int
	for v := 0; v < len(f.tout); v++ {
		for h := 0; h < len(f.tout[0]); h++ {

			if v == 0 || h == 0 || v == len(f.tout)-1 || h == len(f.tout[0])-1 {
				continue
			}
			res = append(res, calc_visible(f, v, h))
		}
	}
	sort.Ints(res)
	//fmt.Println(res[len(res)-1])
	return res[len(res)-1]
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
