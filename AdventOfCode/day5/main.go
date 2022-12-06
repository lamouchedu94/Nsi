package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	j, err := read("input1.txt", 9)
	//_ = tabinstruc
	if err != nil {
		fmt.Println(err)
	}
	run1(j)
	fmt.Println()
	j, err = read("input1.txt", 9)
	//_ = tabinstruc
	if err != nil {
		fmt.Println(err)
	}
	run2(j)

}

type jeux struct {
	quai         []pile
	instructions []instruct
}

type pile []byte
type instruct struct {
	quantite, de, vers int
}

func run1(j jeux) {
	for _, inst := range j.instructions {
		for i := 0; i < inst.quantite; i++ {
			abouger := j.quai[inst.de][0]
			j.quai[inst.de] = j.quai[inst.de][1:]
			j.quai[inst.vers] = append(pile{abouger}, j.quai[inst.vers]...)
		}
	}
	fmt.Print("Part 1 : ")
	for _, q := range j.quai {
		_ = q
		fmt.Print(string(q[0]))
	}
}

func run2(j jeux) {
	for _, inst := range j.instructions {
		abouger := make(pile, inst.quantite)
		copy(abouger, j.quai[inst.de][0:inst.quantite])
		j.quai[inst.de] = j.quai[inst.de][inst.quantite:]
		j.quai[inst.vers] = append(abouger, j.quai[inst.vers]...)

	}
	fmt.Print("Part 2 : ")
	for _, q := range j.quai {
		_ = q
		fmt.Print(string(q[0]))
	}
}

func read(path string, stacks int) (jeux, error) {
	var j jeux

	//initiliser le jeux
	for i := 0; i < stacks; i++ {
		j.quai = append(j.quai, pile{})
	}

	file, err := os.Open(path)
	if err != nil {
		return j, err
	}
	defer file.Close()
	test := bufio.NewScanner(file)
	test.Split(bufio.ScanLines)
out:
	for test.Scan() {
		ligne := test.Bytes()
		for c := 0; c <= stacks; c++ {
			pos := 4*c + 1
			if pos < len(ligne) {
				if ligne[pos] == '1' {
					break out
				}
				if ligne[pos] != ' ' {
					j.quai[c] = append(j.quai[c], ligne[pos])
				}
			}
		}

	}
	if test.Err() != nil {
		return j, test.Err()
	}
	for test.Scan() {
		ligne := test.Text()
		if ligne == "" {
			continue
		}
		m := instruct{}
		fmt.Sscanf(ligne, "move %d from %d to %d", &m.quantite, &m.de, &m.vers)
		if m.quantite != 0 {
			m.de--
			m.vers--
			j.instructions = append(j.instructions, m)
		}

	}
	return j, nil
}
