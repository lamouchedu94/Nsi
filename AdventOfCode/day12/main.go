package main

import (
	"bufio"
	"fmt"
	"os"
)

type Elves struct {
	x         int
	y         int
	elevation byte
}

type mov struct {
	u bool
	d bool
	l bool
	r bool
}

func main() {
	tab, err := read("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	print(tab)

	//tab[y][x]
	run(tab)
}

func run(carte [][]byte) {
	elv := Elves{x: 1, y: 1, elevation: carte[1][1]}
	movmnt := [][]int{}
	fmt.Println(calc_mov(carte, elv, movmnt))

}

func in(elv Elves, mov [][]int) bool {
	for _, move := range mov {
		if move[0] == elv.x && move[1] == elv.y {
			return false
		}
	}
	return true
}

func calc_mov(carte [][]byte, elv Elves, movmnt [][]int) int {
	p := possbilite_mov(carte, elv)
	fmt.Println(elv)
	if p.d {
		if in(elv, movmnt) {
			movmnt = append(movmnt, []int{elv.x, elv.y})
			elv.y++
			calc_mov(carte, elv, movmnt)
		}

	}
	if p.u {
		if in(elv, movmnt) {
			movmnt = append(movmnt, []int{elv.x, elv.y})
			elv.y--
			calc_mov(carte, elv, movmnt)
		}
	}
	if p.l {
		if in(elv, movmnt) {
			movmnt = append(movmnt, []int{elv.x, elv.y})
			elv.x--
			calc_mov(carte, elv, movmnt)
		}
	}
	if p.r {
		if in(elv, movmnt) {
			movmnt = append(movmnt, []int{elv.x, elv.y})
			elv.x++
			calc_mov(carte, elv, movmnt)
		}
	}
	return -1
}

func possbilite_mov(carte [][]byte, elv Elves) mov {
	p := mov{}

	if abs(int(elv.elevation)-int(carte[elv.y+1][elv.x])) == 1 { //down
		p.d = true
	}
	if abs(int(elv.elevation)-int(carte[elv.y-1][elv.x])) == 1 { //up
		p.u = true
	}
	if abs(int(elv.elevation)-int(carte[elv.y][elv.x-1])) == 1 { //left
		p.l = true
	}
	if abs(int(elv.elevation)-int(carte[elv.y][elv.x+1])) == 1 { //right
		p.r = true
	}

	return p

	/*
		fmt.Println(carte[elv.y][elv.x])
		//down
		fmt.Println(carte[elv.y+1][elv.x])
		//up
		fmt.Println(carte[elv.y-1][elv.x])
		//left
		fmt.Println(carte[elv.y][elv.x-1])
		//right
		fmt.Println(carte[elv.y][elv.x+1])
	*/
}

func abs(num int) int {
	if num > 0 {
		return num
	}
	return -num
}

func print(carte [][]byte) {
	for _, c := range carte {
		fmt.Println(c)
	}
}

func read(path string) ([][]byte, error) {
	var tab [][]byte
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	data := bufio.NewScanner(file)

	for data.Scan() {
		tab = append(tab, data.Bytes())
		//fmt.Println(data.Bytes())
	}
	return tab, nil
}
