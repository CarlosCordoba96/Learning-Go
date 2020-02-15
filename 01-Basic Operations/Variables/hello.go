package main
import "fmt"


func main() {
    fmt.Println("hello world")
    for i := 0; i < 10; i++ {
    if i%2==0 {
        fmt.Println("El numero",i," es par")
    }
    }
}