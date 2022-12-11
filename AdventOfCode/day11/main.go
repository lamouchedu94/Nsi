package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	tab, err := read("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(tab)

}

type monkey struct {
	items             []int
	operation         string
	num_for_operation int
	test              int
	iftrue            int
	iffalse           int
}

func read(path string) ([]monkey, error) {
	var tab []monkey
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()
	data := bufio.NewScanner(file)
	num_monkey := 0
	i := 0
	tab = append(tab, monkey{})
	for data.Scan() {
		if i%7 == 0 && i != 0 {
			num_monkey++
			tab = append(tab, monkey{})
		}
		raw := data.Text()
		if len(raw) > 10 {
			switch {
			case raw[:10] == "  Starting":
				text := strings.TrimPrefix(data.Text(), "  Starting items: ")
				temp := strings.Split(text, ", ")
				for _, num := range temp {
					a, _ := strconv.Atoi(num)
					tab[num_monkey].items = append(tab[num_monkey].items, a)
				}
			case raw[:23] == "  Operation: new = old ":
				fmt.Sscanf(raw, "  Operation: new = old %s %d", &tab[num_monkey].operation, &tab[num_monkey].num_for_operation)
			case raw[:17] == "  Test: divisible":
				fmt.Sscanf(raw, "  Test: divisible by %d", &tab[num_monkey].test)
			case raw[:13] == "    If true: ":
				fmt.Sscanf(raw, "    If true: throw to monkey %d", &tab[num_monkey].iftrue)
			case raw[:14] == "    If false: ":
				fmt.Sscanf(raw, "    If false: throw to monkey %d", &tab[num_monkey].iffalse)
			}
		}

		i++
	}
	return tab, err

}
