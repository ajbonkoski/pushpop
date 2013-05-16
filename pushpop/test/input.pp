        push 16
        popsp
        push 0
        dup
        store

        push 1234
        push 5678
        push 0
        flip
        sub
        sub
        push 1
        sub
        dup
        dup
        dup
        dup
        nand

        push 0
        flip
        sub
        sub

        push 0
        flip
        sub
        sub

        pushsp
        pushsp
        
        push 1
        push 0
        flip
        sub



        push 12
        push 0
        store
        
        push 1
        push 1
        store

        push 0
        load
        push 1
        load
        push 0
        flip
        sub
        sub
        push 0
        store

        push 1
        push 0
        flip
        sub
        push 1
        push 1
        shift

        push 12

        dup
        push 28
        push 0
        shift

        dup
        push 28
        push 1
        shift

        dup
        push 15
        nand
        dup
        nand

        halt
