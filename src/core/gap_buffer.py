from __future__ import annotations

class GapBuffer:
    def __init__(self,capacity = 64):
        self.capacity = capacity
        self.buff = ['']*self.capacity
        self.gap_start = 0
        self.gap_end = self.capacity
    
    def gap_len(self)->int:
        "It gives the gap length"
        return self.gap_end-self.gap_start

    def __len__(self)->int :
        return len(self.buff) - self.gap_len()

    def __grow(self) :

        left_text = self.buff[:self.gap_start]
        right_text = self.buff[self.gap_end:]

        self.capacity *=2 
        self.gap_end = self.capacity-len(right_text)
        new_buff = [""]*self.capacity        

        #copying the ele frm both side to new buff
        new_buff[:self.gap_start] = left_text
        new_buff[self.gap_end:] = right_text

        self.buff = new_buff

    def insert(self,val) :
        if not self.gap_len():
            self.__grow()

        self.buff[self.gap_start] = val
        self.gap_start += 1

    def __move_left(self):
        """
        Moves the gap to the left side 
            the gap start is at 3
            ["a","b","c","_","_","_","d","e","f"]

            need to mv the gap start to 2
            ["a","b","_","_","_","c","d","e","f"]

        copy the char before the gap_start and paste at the pos after the gap_ends
        """
        self.buff[self.gap_end-1] = self.buff[self.gap_start-1]
        self.buff[self.gap_start-1] = ""
        self.gap_start -= 1
        self.gap_end -= 1

    def __move_right(self):
        """
        Move the gap to the right side,
        Sames logic we copy the gap_end+1 and put it at gap_start and then inc gap_start and gap_end
        Here the gap starts at 1 we need to mv that to 3
        ['x', '', '', '', 'a', 'r']

        ['x','a','r','','','']
        """

        self.buff[self.gap_start]=self.buff[self.gap_end]
        self.buff[self.gap_end] = ''
        self.gap_start +=1
        self.gap_end +=1


    def move_gap(self,position:int):
        """It moves the Gap to given position"""

        #first validate the tar_position
        if position < 0 or position > len(self):
            raise IndexError("The Position is out of range")
        #check gap,if no gap then grow gap
        if not self.gap_len():
            self.__grow()

        #move the buff based on the gap_start and tar_pos
        while (position != self.gap_start):
            if position < self.gap_start:
                self.__move_left()
            elif position > self.gap_start:
                self.__move_right() 

    def delete_forward(self):

        "Delete the char after the gap"
        if self.gap_end < self.capacity:
            self.gap_end += 1

    def delete_backward(self):
        "Delete the char before the gap"
        if self.gap_start > 0:
            self.gap_start -= 1

    def delete(self,position,cnt = 1):

        if position < 0 or position > len(self):
            raise IndexError("The position is out of range")
        if cnt <= len(self)-position and cnt > 0: 
            self.move_gap(position)
            while cnt:
                self.delete_forward()
                cnt-=1
        else:
            raise ValueError("Delete count is invalid") 

    def get_text(self)->str:

        left_half = self.buff[:self.gap_start]
        right_half = self.buff[self.gap_end:]
        return "".join(left_half+right_half)


if __name__ == "__main__":

    gb2=GapBuffer(6)
    gb2.insert('x')
    gb2.insert('a')
    gb2.insert('r') 
    print(len(gb2.buff))
    print(gb2.gap_start)
    print("moving to left side")
    gb2.move_gap(1) #gap start is at 3, now i will move it to 1
    print(gb2.gap_start)
    print(gb2.buff)
    print("moving to right side")
    gb2.move_gap(3)
    print(gb2.gap_start)

    for p in (-5, 999):
        try: 
            gb2.move_gap(p) 
            print(f'move_gap({p}): no error (bounds check dead)')
        except IndexError: 
            print(f'move_gap({p}): IndexError raised ok')

    print()


