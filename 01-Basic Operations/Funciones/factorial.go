package main

import "fmt"
import "os"
import "strconv"

func factorial_recursivo (facto uint64)  uint64{
	if facto>1 {
		return facto*factorial_recursivo(facto-1)

	}else {
		return 1
	}

}

func main() {
	number,_:=strconv.ParseUint(os.Args[1],10,64)
	fmt.Println(factorial_recursivo(number))
}