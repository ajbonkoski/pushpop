        push 1
loop    dup
        push -1
        sub
        dup
        push 5
        sub
        ble loop
        halt
