def move_crates(filename, multiple=False):
    with open(filename) as newFile:
        lines =  [ line for line in newFile.readlines()]
        crates = lines[:lines.index("\n")]
        splitCrates = [stack.replace("\n", "") for stack in crates]
        
        newCrates =  [stack[1::4] for stack in splitCrates]
        numStacks = len(newCrates.pop()) -1

        stacks = []
        for stack in newCrates:
            for i, crate in enumerate(stack):
                if len(stacks) <= i:
                    stacks.append([])
                if (crate.split()):
                    stacks[i].append(crate)


        reversedStacks = [stack.reverse() for stack in stacks]

        # Instructions
        instructions = lines[lines.index("\n"):]
        instructions.remove("\n")

        for instruction in instructions:
            instruction = instruction.replace("move", "").replace("from", "").replace("to", "")
            # print(instruction)
       
        parsedInstructions = [[int(i) for i in instruction.replace("move", "").replace("from", "").replace("to", "").split()] for instruction in instructions]

        for instruction in parsedInstructions:

            if multiple:
                if len(stacks[instruction[1] - 1]) >= instruction[0]:
                    stacks[instruction[2] -1] = stacks[instruction[2] -1] + stacks[instruction[1]-1][len(stacks[instruction[1]-1]) - instruction[0]:]
                    stacks[instruction[1] - 1] = stacks[instruction[1]-1][:len(stacks[instruction[1]-1]) - instruction[0]]
            else:
                for i in range(0, instruction[0]):
                    if len(stacks[instruction[1] - 1]) > 0:
                        stacks[instruction[2] - 1].append(stacks[instruction[1] - 1].pop())
        
        return ''.join([stack.pop() for stack in stacks if len(stack) > 0])
        # return stacks

print(move_crates('inputs/problem_5.txt', True))
