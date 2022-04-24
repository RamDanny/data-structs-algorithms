import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if len(self.cells) == self.count:
            return self.cells
        else:
            return None
        #raise NotImplementedError

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if self.count == 0:
            return self.cells
        else:
            return None
        #raise NotImplementedError

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1
        #raise NotImplementedError

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)
        #raise NotImplementedError


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for know in self.knowledge:
            know.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for know in self.knowledge:
            know.mark_safe(cell)

    # if any subset inferences are possible from knowledge base alone
    def knowledge_update(self, knowledge):
        if knowledge == None:
            return
        for sentence in knowledge:
            # detect any remaining mines/safes
            if len(sentence.cells) == sentence.count:
                for cell in sentence.cells:
                    self.mines.add(cell)
                knowledge.remove(sentence)
            elif sentence.count == 0:
                for cell in sentence.cells:
                    self.safes.add(cell)
                knowledge.remove(sentence)
        
        for i in range(len(knowledge)):
            for j in range(i+1, len(knowledge)):
                if knowledge[i].cells < knowledge[j].cells:
                    # inference drawn by subset subtraction
                    diffcells = knowledge[j].cells - knowledge[i].cells
                    diffcount = knowledge[j].count - knowledge[i].count
                    # if any inference is all mines
                    if len(diffcells) == diffcount:
                        for cell in diffcells:
                            self.mark_mine(cell)
                    # if any inference is all safes
                    elif diffcount == 0:
                        for cell in diffcells:
                            self.mark_safe(cell)
                    else:
                        if Sentence(diffcells, diffcount) not in knowledge:
                            knowledge.append(Sentence(diffcells, diffcount))
                
                elif knowledge[j].cells < knowledge[i].cells:
                    # inference drawn by subset subtraction
                    diffcells = knowledge[i].cells - knowledge[j].cells
                    diffcount = knowledge[i].count - knowledge[j].count
                    # if any inference is all mines
                    if len(diffcells) == diffcount:
                        for cell in diffcells:
                            self.mark_mine(cell)
                    # if any inference is all safes
                    elif diffcount == 0:
                        for cell in diffcells:
                            self.mark_safe(cell)
                    else:
                        if Sentence(diffcells, diffcount) not in knowledge:
                            knowledge.append(Sentence(diffcells, diffcount))

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        ### mark cell as a move made
        self.moves_made.add(cell)
        ### mark the cell as safe
        self.mark_safe(cell)
        ### add new sentence to knowledge based on cell's neighbours
        cells = set()
        # find neighbours
        for i in range(cell[0]-1, cell[0]+2):
            for j in range(cell[1]-1, cell[1]+2):
                if i >= 0 and i < self.width and j >= 0 and j < self.width:
                    if (i, j) != cell:
                        cells.add((i, j))
        newcells = cells.copy()
        newcount = int(count)
        # if all neighbours are safes
        if newcount == 0:
            for cell in newcells:
                self.mark_safe(cell)
        # if all neighbours are mines
        elif newcount == len(newcells):
            for cell in newcells:
                self.mark_mine(cell)
        else:
            # if any existing mines or safes present in neighbours
            for cell in cells:
                if cell in self.mines:
                    newcells.remove(cell)
                    newcount -= 1
                elif cell in self.safes:
                    newcells.remove(cell)
            # if any subset inference is possible
            for sentence in self.knowledge:
                if newcells < sentence.cells:
                    # inference drawn by subset subtraction
                    diffcells = sentence.cells - newcells
                    diffcount = sentence.count - newcount
                    # if any inference is all mines
                    if len(diffcells) == diffcount:
                        for cell in diffcells:
                            self.mark_mine(cell)
                    # if any inference is all safes
                    elif diffcount == 0:
                        for cell in diffcells:
                            self.mark_safe(cell)
                    else:
                        if Sentence(diffcells, diffcount) not in self.knowledge:
                            self.knowledge.append(Sentence(diffcells, diffcount))
                
                elif sentence.cells < newcells:
                    # inference drawn by subset subtraction
                    diffcells = newcells - sentence.cells
                    diffcount = newcount - sentence.count
                    # if any inference is all mines
                    if len(diffcells) == diffcount:
                        for cell in diffcells:
                            self.mark_mine(cell)
                    # if any inference is all safes
                    elif diffcount == 0:
                        for cell in diffcells:
                            self.mark_safe(cell)
                    else:
                        if Sentence(diffcells, diffcount) not in self.knowledge:
                            self.knowledge.append(Sentence(diffcells, diffcount))
        
            # after all inferences from neighbours of given cell
            # if there are new inferences from knowledge base
            self.knowledge_update(self.knowledge)
        #raise NotImplementedError

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        if self.safes == None:
            return None
        for cell in self.safes:
            if cell not in self.moves_made:
                return cell
        #raise NotImplementedError

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        done = False
        checked = set()
        while done == False and len(checked) <= self.height * self.width:
            i = random.randrange(0, self.height)
            j = random.randrange(0, self.width)
            if (i, j) not in self.moves_made and (i, j) not in self.mines:
                done = True
            else:
                checked.add((i, j))
        if done == True:
            return (i, j)
        else:
            return None
        #raise NotImplementedError

    