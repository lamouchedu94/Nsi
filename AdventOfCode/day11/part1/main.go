package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	tab, err := read("../input1.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(tab)
	run(tab)
	var tab_inspect []int
	for _, m := range tab {
		tab_inspect = append(tab_inspect, m.inspect)
	}
	sort.Ints(tab_inspect)
	res := tab_inspect[len(tab_inspect)-1] * tab_inspect[len(tab_inspect)-2]
	print(tab)
	fmt.Println(res)

}

func print(tab []*monkey) {
	for _, t := range tab {
		fmt.Println(t.items)
	}
}

type monkey struct {
	items             []int
	operation         string
	num_for_operation int
	divisor           int
	iftrue            int
	iffalse           int
	inspect           int
}

func run(monkeys []*monkey) {
	for j := 0; j < 10000; j++ {
		for i, m := range monkeys {
			for _, item := range m.items {
				switch {
				case m.num_for_operation == 0:
					item = item * item
				case m.operation == "*":
					item = item * m.num_for_operation
				case m.operation == "+":
					item = item + m.num_for_operation

				}
				item = item / 3
				m.inspect += 1
				if item%m.divisor == 0 {
					monkeys[m.iftrue].items = append(monkeys[m.iftrue].items, item)
				} else {
					monkeys[m.iffalse].items = append(monkeys[m.iffalse].items, item)
				}

			}
			monkeys[i].items = []int{}
		}
	}

}

func read(path string) ([]*monkey, error) {
	var tab []*monkey
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()
	data := bufio.NewScanner(file)
	num_monkey := 0
	i := 0
	tab = append(tab, &monkey{})
	for data.Scan() {
		if i%7 == 0 && i != 0 {
			num_monkey++
			tab = append(tab, &monkey{})
		}
		raw := data.Text()
		if len(raw) > 10 {
			switch {
			case strings.HasPrefix(raw, "  Starting"):
				text := strings.TrimPrefix(data.Text(), "  Starting items: ")
				temp := strings.Split(text, ", ")
				for _, num := range temp {
					a, _ := strconv.Atoi(num)
					tab[num_monkey].items = append(tab[num_monkey].items, a)
				}
			case strings.HasPrefix(raw, "  Operation: new = old "):
				fmt.Sscanf(raw, "  Operation: new = old %s %d", &tab[num_monkey].operation, &tab[num_monkey].num_for_operation)
			case strings.HasPrefix(raw, "  Test: divisible"):
				fmt.Sscanf(raw, "  Test: divisible by %d", &tab[num_monkey].divisor)
			case strings.HasPrefix(raw, "    If true: "):
				fmt.Sscanf(raw, "    If true: throw to monkey %d", &tab[num_monkey].iftrue)
			case strings.HasPrefix(raw, "    If false: "):
				fmt.Sscanf(raw, "    If false: throw to monkey %d", &tab[num_monkey].iffalse)
			}
		}

		i++
	}
	return tab, err

}

/*
2637590098
2713310158
*/
