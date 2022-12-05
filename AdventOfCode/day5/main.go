package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	tab, tabinstruc, err := read("input1.txt")
	_ = tabinstruc
	if err != nil {
		fmt.Println(err)
	}

	run(tab, tabinstruc)
	//fmt.Println(tab[1])
	//fmt.Println(tabinstruc)
}

type instruct struct {
	a, b, c, d, e, f, g, h, i, j int
}

// DNZ
// CM
// P DNZ

func run(tab []string, tabinstruc []instruct) {
	for _, t := range tabinstruc {
		for i := 0; i < t.a; i++ {
			//bouge depuis le 2 de 0
			var abouger string
			if len(string(tab[t.b-1])) > 0 {
				abouger = string(tab[t.b-1][0])
			}

			//valeur de la pile 1 en supprimant le truc le plus haut si espace
			var temp string
			if len(string(tab[t.c-1])) > 0 {
				if string(tab[t.c-1][0]) == " " {
					var ind int
					for _, car := range tab[t.c-1] {
						if string(car) == " " {
							ind += 1
						}
					}
					temp = tab[t.c-1][ind:len(tab[t.c-1])]

				} else {
					temp = tab[t.c-1]
				}
			}
			tab[t.c-1] = abouger + temp
			tab[t.b-1] = tab[t.b-1][1:len(tab[t.b-1])]

			fmt.Println(tab[0:9])
		}
	}

}

func decoupage(line string, tab []string) []string {
	j := 0
	for i := 1; i < 35; i += 4 {
		if string(line[i]) != " " {
			tab[j] += string(line[i])
		} else {
			tab[j] += " "
		}
		j += 1
	}
	return tab
	/*
		if string(line[1]) != " " {
			tab[0] += string(line[1])
		} else {
			tab[0] += " "
		}
		if string(line[5]) != " " {
			tab[1] += string(line[5])
		} else {
			tab[1] += " "
		}
		if string(line[9]) != " " {
			tab[2] += string(line[9])
		} else {
			tab[2] += " "
		}
		return tab
	*/
}
func read(path string) ([]string, []instruct, error) {
	var tab []string
	var tabinstruction []instruct
	fin := true

	//var colonne []string
	for i := 0; i < 9; i++ {
		temp := []string{""}
		tab = append(tab, temp...)
	}

	file, err := os.Open(path)
	if err != nil {
		return nil, nil, err
	}
	defer file.Close()
	test := bufio.NewScanner(file)
	test.Split(bufio.ScanLines)
	for test.Scan() {

		if test.Text() == " 1   2   3   4   5   6   7   8   9 " {
			fin = false

		}
		if fin {
			tab = decoupage(test.Text(), tab)
			tab = append(tab, test.Text())
		} else {
			line := test.Text()
			m := instruct{}
			fmt.Sscanf(line, "move %d from %d to %d", &m.a, &m.b, &m.c, &m.d, &m.e, &m.f, &m.g, &m.h, &m.i, &m.j)
			if m.a != 0 {
				tabinstruction = append(tabinstruction, m)
			}

		}

	}
	return tab, tabinstruction, err
}
