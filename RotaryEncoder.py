class RotaryEncoder():
    count=0
    pi_count=50 # 100パルス/回転
    state=0
    state_map = {
        'initial': 0,
        'cw_1': 1,
        'cw_2': 2,
        'cw_3': 3,
        'ccw_1': 4,
        'ccw_2': 5,
        'ccw_3': 6,
    }
    def init_count(self):
        self.count=0
        self.state=0
    def get_rad(self):
        return 3.14159 * self.count / self.pi_count
    def update_state(self,cha, chb):
        if cha == 0 and chb == 0:
            if self.state==self.state_map["cw_3"]:
                self.count=self.count+1
            elif self.state==self.state_map["ccw_3"]:
                self.count=self.count-1
            self.state=self.state_map["initial"]
        else:
            if self.state == self.state_map["initial"]:
                if cha == 1 and chb == 0:
                    self.state=self.state_map["cw_1"]
                elif cha == 0 and chb == 1:
                    self.state=self.state_map["ccw_1"]
            elif self.state == self.state_map["cw_1"] or self.state == self.state_map["cw_3"]:
                if cha == 1 and chb == 1:
                    self.state=self.state_map["cw_2"]
                # elif cha == 0 and chb == 0:
                #     self.state=self.state_map["initial"]
            elif self.state == self.state_map["cw_2"]:
                if cha == 0 and chb == 1:
                    self.state=self.state_map["cw_3"]
                elif cha == 1 and chb == 0:
                    self.state=self.state_map["cw_1"]          
            elif self.state == self.state_map["ccw_1"] or self.state == self.state_map["ccw_3"]:
                if cha == 1 and chb == 1:
                    self.state=self.state_map["ccw_2"]
                # elif cha == 0 and chb == 0:
                #     self.state=self.state_map["initial"]
            elif self.state == self.state_map["ccw_2"]:
                if cha == 0 and chb == 1:
                    self.state=self.state_map["ccw_1"]
                elif cha == 1 and chb == 0:
                    self.state=self.state_map["ccw_3"]
        return self.get_rad()
