# NOTE: yo b() is huffman-19, just extract a() aka huffman-20 and run the script, you will get the flag
# i m too lazy to do that


curr = 0
bit_buffer = 0
bit_count = 0
stream_data = 0

def ensure_bits(i):
    global curr, bit_buffer, bit_count, stream_data
    while bit_count < i:
        if curr >= len(stream_data):
            exit()
        bit_buffer = ((bit_buffer << 8) | (stream_data[curr] & 0xFF)) & 0xFFFFFFFFFFFFFFFF

        curr += 1
        bit_count += 8

    if curr == 1889328:
      bit_buffer = 18446744073709551615  

def b():
  global curr, bit_buffer, bit_count, stream_data

  ensure_bits(19)
  if (((bit_buffer >> (bit_count - 1)) & 1) == 1) :
    if (((bit_buffer >> (bit_count - 2)) & 1) == 1) :
      bit_count -= 2
      return 0
    
    if (((bit_buffer >> (bit_count - 3)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 4)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 5)) & 1) == 1) :
          bit_count -= 5
          return 128
        
        bit_count -= 5
        return 7
      
      if (((bit_buffer >> (bit_count - 5)) & 1) == 1) :
        bit_count -= 5
        return 31
      
      if (((bit_buffer >> (bit_count - 6)) & 1) == 1) :
        bit_count -= 6
        return 63
      
      bit_count -= 6
      return 240
    
    if (((bit_buffer >> (bit_count - 4)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 5)) & 1) == 1) :
        bit_count -= 5
        return 127
      
      bit_count -= 5
      return 224
    
    if (((bit_buffer >> (bit_count - 5)) & 1) == 1) :
      bit_count -= 5
      return 248
    
    if (((bit_buffer >> (bit_count - 6)) & 1) == 1) :
      bit_count -= 6
      return 252
    
    if (((bit_buffer >> (bit_count - 7)) & 1) != 1) :
      if (((bit_buffer >> (bit_count - 8)) & 1) != 1) :
        if (((bit_buffer >> (bit_count - 9)) & 1) == 1) :
          bit_count -= 9
          return 64
        
        if (((bit_buffer >> (bit_count - 10)) & 1) != 1) :
          if (((bit_buffer >> (bit_count - 11)) & 1) == 1) :
            bit_count -= 11
            return 195
          
          if (((bit_buffer >> (bit_count - 12)) & 1) != 1) :
            if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
              bit_count -= 13
              return 238
            
            bit_count -= 13
            return 228
          
          if (((bit_buffer >> (bit_count - 13)) & 1) != 1) :
            bit_count -= 13
            return 184
          
          if (((bit_buffer >> (bit_count - 14)) & 1) != 1) :
            bit_count -= 14
            return 76
          
          if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
            bit_count -= 15
            return 58
          
          if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
            bit_count -= 16
            return 107
          
          bit_count -= 16
          return 150
        
        if (((bit_buffer >> (bit_count - 11)) & 1) == 1) :
          if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
            bit_count -= 12
            return 134
          
          if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
            bit_count -= 13
            return 246
          
          bit_count -= 13
          return 156
        
        if (((bit_buffer >> (bit_count - 12)) & 1) != 1) :
          if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
            bit_count -= 13
            return 232
          
          bit_count -= 13
          return 194
        
        if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
          bit_count -= 13
          return 51
        
        if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
          bit_count -= 14
          return 108
        
        if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
          if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
            bit_count -= 16
            return 117
          
          bit_count -= 16
          return 83
        
        if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
          bit_count -= 16
          return 205
        
        bit_count -= 16
        return 202
      
      if (((bit_buffer >> (bit_count - 9)) & 1) == 1) :
        bit_count -= 9
        return 2
      
      if (((bit_buffer >> (bit_count - 10)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 11)) & 1) == 1) :
          if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
            bit_count -= 12
            return 97
          
          if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
            bit_count -= 13
            return 29
          
          bit_count -= 13
          return 80
        
        if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
          bit_count -= 12
          return 152
        
        if (((bit_buffer >> (bit_count - 13)) & 1) != 1) :
          bit_count -= 13
          return 119
        
        if (((bit_buffer >> (bit_count - 14)) & 1) != 1) :
          bit_count -= 14
          return 18
        
        if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
          if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
            bit_count -= 16
            return 89
          
          bit_count -= 16
          return 172
        
        if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
          bit_count -= 16
          return 86
        
        bit_count -= 16
        return 77
      
      if (((bit_buffer >> (bit_count - 11)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 12)) & 1) != 1) :
          bit_count -= 12
          return 5
        
        if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
          bit_count -= 13
          return 113
        
        if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
          bit_count -= 14
          return 70
        
        bit_count -= 14
        return 68
      
      if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
        bit_count -= 12
        return 103
      
      if (((bit_buffer >> (bit_count - 13)) & 1) != 1) :
        bit_count -= 13
        return 23
      
      if (((bit_buffer >> (bit_count - 14)) & 1) != 1) :
        bit_count -= 14
        return 118
      
      if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
          bit_count -= 16
          return 197
        
        bit_count -= 16
        return 81
      
      if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
        bit_count -= 16
        return 168
      
      bit_count -= 16
      return 141
    
    if (((bit_buffer >> (bit_count - 8)) & 1) != 1) :
      if (((bit_buffer >> (bit_count - 9)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 10)) & 1) == 1) :
          bit_count -= 10
          return 112
        
        if (((bit_buffer >> (bit_count - 11)) & 1) == 1) :
          bit_count -= 11
          return 239
        
        if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
          if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
            bit_count -= 13
            return 57
          
          bit_count -= 13
          return 176
        
        if (((bit_buffer >> (bit_count - 13)) & 1) != 1) :
          bit_count -= 13
          return 208
        
        if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
          bit_count -= 14
          return 79
        
        if (((bit_buffer >> (bit_count - 15)) & 1) != 1) :
          bit_count -= 15
          return 153
        
        if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
          bit_count -= 16
          return 233
        
        bit_count -= 16
        return 147
      
      if (((bit_buffer >> (bit_count - 10)) & 1) == 1) :
        bit_count -= 10
        return 14
      
      if (((bit_buffer >> (bit_count - 11)) & 1) == 1) :
        bit_count -= 11
        return 191
      
      if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
          bit_count -= 13
          return 111
        
        if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
          bit_count -= 14
          return 20
        
        bit_count -= 14
        return 88
      
      if (((bit_buffer >> (bit_count - 13)) & 1) != 1) :
        if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
          bit_count -= 14
          return 61
        
        bit_count -= 14
        return 242
      
      if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
        bit_count -= 14
        return 188
      
      if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
        bit_count -= 15
        return 122
      
      if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
        bit_count -= 16
        return 201
      
      if (((bit_buffer >> (bit_count - 17)) & 1) == 1) :
        bit_count -= 17
        return 165
      
      bit_count -= 17
      return 173
    
    if (((bit_buffer >> (bit_count - 9)) & 1) != 1) :
      if (((bit_buffer >> (bit_count - 10)) & 1) != 1) :
        bit_count -= 10
        return 56
      
      if (((bit_buffer >> (bit_count - 11)) & 1) == 1) :
        bit_count -= 11
        return 247
      
      if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
          bit_count -= 13
          return 158
        
        bit_count -= 13
        return 136
      
      if (((bit_buffer >> (bit_count - 13)) & 1) != 1) :
        bit_count -= 13
        return 140
      
      if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
        bit_count -= 14
        return 104
      
      if (((bit_buffer >> (bit_count - 15)) & 1) != 1) :
        if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
          bit_count -= 16
          return 175
        
        bit_count -= 16
        return 73
      
      if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
        bit_count -= 16
        return 82
      
      if (((bit_buffer >> (bit_count - 17)) & 1) == 1) :
        bit_count -= 17
        return 171
      
      bit_count -= 17
      return 180
    
    if (((bit_buffer >> (bit_count - 10)) & 1) != 1) :
      bit_count -= 10
      return 28
    
    if (((bit_buffer >> (bit_count - 11)) & 1) != 1) :
      bit_count -= 11
      return 223
    
    if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 13)) & 1) != 1) :
        bit_count -= 13
        return 198
      
      if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
        bit_count -= 14
        return 100
      
      bit_count -= 14
      return 34
    
    if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 14)) & 1) != 1) :
        bit_count -= 14
        return 72
      
      if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
        bit_count -= 15
        return 219
      
      if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
        bit_count -= 16
        return 215
      
      bit_count -= 16
      return 167
    
    if (((bit_buffer >> (bit_count - 14)) & 1) != 1) :
      if (((bit_buffer >> (bit_count - 15)) & 1) != 1) :
        bit_count -= 15
        return 116
      
      if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
        bit_count -= 16
        return 90
      
      bit_count -= 16
      return 221
    
    if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
        bit_count -= 16
        return 163
      
      bit_count -= 16
      return 145
    
    if (((bit_buffer >> (bit_count - 16)) & 1) != 1) :
      bit_count -= 16
      return 91
    
    if (((bit_buffer >> (bit_count - 17)) & 1) == 1) :
      bit_count -= 17
      return 45
    
    if (((bit_buffer >> (bit_count - 18)) & 1) != 1) :
      bit_count -= 18
      return 181
    
    if (((bit_buffer >> (bit_count - 19)) & 1) == 1) :
      bit_count -= 19
      return 169
    
    bit_count -= 19
    return 65535
  
  if (((bit_buffer >> (bit_count - 2)) & 1) == 1) :
    bit_count -= 2
    return 255
  
  if (((bit_buffer >> (bit_count - 3)) & 1) != 1) :
    if (((bit_buffer >> (bit_count - 4)) & 1) == 1) :
      bit_count -= 4
      return 1
    
    if (((bit_buffer >> (bit_count - 5)) & 1) == 1) :
      bit_count -= 5
      return 192
    
    bit_count -= 5
    return 15
  
  if (((bit_buffer >> (bit_count - 4)) & 1) != 1) :
    if (((bit_buffer >> (bit_count - 5)) & 1) == 1) :
      bit_count -= 5
      return 3
    
    if (((bit_buffer >> (bit_count - 6)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 7)) & 1) != 1) :
        if (((bit_buffer >> (bit_count - 8)) & 1) == 1) :
          bit_count -= 8
          return 6
        
        bit_count -= 8
        return 96
      
      if (((bit_buffer >> (bit_count - 8)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 9)) & 1) == 1) :
          bit_count -= 9
          return 126
        
        bit_count -= 9
        return 231
      
      if (((bit_buffer >> (bit_count - 9)) & 1) != 1) :
        bit_count -= 9
        return 249
      
      if (((bit_buffer >> (bit_count - 10)) & 1) == 1) :
        bit_count -= 10
        return 199
      
      bit_count -= 10
      return 143
    
    if (((bit_buffer >> (bit_count - 7)) & 1) != 1) :
      if (((bit_buffer >> (bit_count - 8)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 9)) & 1) == 1) :
          bit_count -= 9
          return 159
        
        bit_count -= 9
        return 225
      
      if (((bit_buffer >> (bit_count - 9)) & 1) != 1) :
        bit_count -= 9
        return 135
      
      if (((bit_buffer >> (bit_count - 10)) & 1) == 1) :
        bit_count -= 10
        return 60
      
      bit_count -= 10
      return 251
    
    if (((bit_buffer >> (bit_count - 8)) & 1) != 1) :
      bit_count -= 8
      return 24
    
    if (((bit_buffer >> (bit_count - 9)) & 1) != 1) :
      if (((bit_buffer >> (bit_count - 10)) & 1) == 1) :
        bit_count -= 10
        return 253
      
      if (((bit_buffer >> (bit_count - 11)) & 1) != 1) :
        bit_count -= 11
        return 25
      
      if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
        bit_count -= 12
        return 13
      
      if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
        bit_count -= 13
        return 47
      
      if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
          bit_count -= 15
          return 161
        
        bit_count -= 15
        return 21
      
      if (((bit_buffer >> (bit_count - 15)) & 1) != 1) :
        bit_count -= 15
        return 157
      
      if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
        bit_count -= 16
        return 42
      
      bit_count -= 16
      return 170
    
    if (((bit_buffer >> (bit_count - 10)) & 1) != 1) :
      bit_count -= 10
      return 241
    
    if (((bit_buffer >> (bit_count - 11)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
        bit_count -= 12
        return 49
      
      if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
        bit_count -= 13
        return 10
      
      bit_count -= 13
      return 244
    
    if (((bit_buffer >> (bit_count - 12)) & 1) != 1) :
      bit_count -= 12
      return 99
    
    if (((bit_buffer >> (bit_count - 13)) & 1) != 1) :
      bit_count -= 13
      return 190
    
    if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
        bit_count -= 15
        return 151
      
      bit_count -= 15
      return 189
    
    if (((bit_buffer >> (bit_count - 15)) & 1) != 1) :
      bit_count -= 15
      return 164
    
    if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
      bit_count -= 16
      return 212
    
    bit_count -= 16
    return 85
  
  if (((bit_buffer >> (bit_count - 5)) & 1) == 1) :
    bit_count -= 5
    return 254
  
  if (((bit_buffer >> (bit_count - 6)) & 1) == 1) :
    if (((bit_buffer >> (bit_count - 7)) & 1) != 1) :
      if (((bit_buffer >> (bit_count - 8)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 9)) & 1) == 1) :
          bit_count -= 9
          return 12
        
        bit_count -= 9
        return 120
      
      if (((bit_buffer >> (bit_count - 9)) & 1) == 1) :
        bit_count -= 9
        return 32
      
      bit_count -= 9
      return 16
    
    if (((bit_buffer >> (bit_count - 8)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 9)) & 1) == 1) :
        bit_count -= 9
        return 4
      
      bit_count -= 9
      return 8
    
    if (((bit_buffer >> (bit_count - 9)) & 1) != 1) :
      if (((bit_buffer >> (bit_count - 10)) & 1) == 1) :
        bit_count -= 10
        return 124
      
      if (((bit_buffer >> (bit_count - 11)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
          if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
            bit_count -= 13
            return 11
          
          bit_count -= 13
          return 55
        
        if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
          bit_count -= 13
          return 200
        
        bit_count -= 13
        return 142
      
      if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
        bit_count -= 12
        return 17
      
      if (((bit_buffer >> (bit_count - 13)) & 1) != 1) :
        bit_count -= 13
        return 67
      
      if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
        bit_count -= 14
        return 44
      
      if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
          bit_count -= 16
          return 166
        
        bit_count -= 16
        return 37
      
      if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
        bit_count -= 16
        return 214
      
      bit_count -= 16
      return 154
    
    if (((bit_buffer >> (bit_count - 10)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 11)) & 1) != 1) :
        if (((bit_buffer >> (bit_count - 12)) & 1) != 1) :
          bit_count -= 12
          return 65
        
        if (((bit_buffer >> (bit_count - 13)) & 1) != 1) :
          bit_count -= 13
          return 204
        
        if (((bit_buffer >> (bit_count - 14)) & 1) != 1) :
          if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
            bit_count -= 15
            return 94
          
          bit_count -= 15
          return 78
        
        if (((bit_buffer >> (bit_count - 15)) & 1) != 1) :
          bit_count -= 15
          return 155
        
        if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
          bit_count -= 16
          return 106
        
        bit_count -= 16
        return 105
      
      if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 13)) & 1) != 1) :
          bit_count -= 13
          return 250
        
        if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
          bit_count -= 14
          return 54
        
        bit_count -= 14
        return 38
      
      if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
        bit_count -= 13
        return 123
      
      if (((bit_buffer >> (bit_count - 14)) & 1) != 1) :
        bit_count -= 14
        return 26
      
      if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
          bit_count -= 16
          return 69
        
        bit_count -= 16
        return 211
      
      if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
        bit_count -= 16
        return 203
      
      bit_count -= 16
      return 179
    
    if (((bit_buffer >> (bit_count - 11)) & 1) != 1) :
      if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
        if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
          bit_count -= 13
          return 36
        
        bit_count -= 13
        return 66
      
      if (((bit_buffer >> (bit_count - 13)) & 1) != 1) :
        bit_count -= 13
        return 222
      
      if (((bit_buffer >> (bit_count - 14)) & 1) != 1) :
        bit_count -= 14
        return 50
      
      if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
        bit_count -= 15
        return 109
      
      if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
        bit_count -= 16
        return 139
      
      bit_count -= 16
      return 178
    
    if (((bit_buffer >> (bit_count - 12)) & 1) != 1) :
      if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
        bit_count -= 13
        return 102
      
      if (((bit_buffer >> (bit_count - 14)) & 1) != 1) :
        bit_count -= 14
        return 52
      
      if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
        bit_count -= 15
        return 133
      
      if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
        bit_count -= 16
        return 75
      
      bit_count -= 16
      return 209
    
    if (((bit_buffer >> (bit_count - 13)) & 1) != 1) :
      bit_count -= 13
      return 39
    
    if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
      bit_count -= 14
      return 22
    
    if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
      bit_count -= 15
      return 217
    
    if (((bit_buffer >> (bit_count - 16)) & 1) != 1) :
      bit_count -= 16
      return 148
    
    if (((bit_buffer >> (bit_count - 17)) & 1) == 1) :
      bit_count -= 17
      return 213
    
    bit_count -= 17
    return 186
  
  if (((bit_buffer >> (bit_count - 7)) & 1) != 1) :
    if (((bit_buffer >> (bit_count - 8)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 9)) & 1) == 1) :
        bit_count -= 9
        return 30
      
      bit_count -= 9
      return 48
    
    if (((bit_buffer >> (bit_count - 9)) & 1) != 1) :
      if (((bit_buffer >> (bit_count - 10)) & 1) != 1) :
        bit_count -= 10
        return 227
      
      if (((bit_buffer >> (bit_count - 11)) & 1) != 1) :
        if (((bit_buffer >> (bit_count - 12)) & 1) != 1) :
          bit_count -= 12
          return 121
        
        if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
          bit_count -= 13
          return 98
        
        bit_count -= 13
        return 206
      
      if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
        bit_count -= 12
        return 132
      
      if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
        bit_count -= 13
        return 71
      
      if (((bit_buffer >> (bit_count - 14)) & 1) != 1) :
        bit_count -= 14
        return 114
      
      if (((bit_buffer >> (bit_count - 15)) & 1) != 1) :
        bit_count -= 15
        return 245
      
      if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
        bit_count -= 16
        return 162
      
      bit_count -= 16
      return 84
    
    if (((bit_buffer >> (bit_count - 10)) & 1) != 1) :
      bit_count -= 10
      return 131
    
    if (((bit_buffer >> (bit_count - 11)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
        bit_count -= 12
        return 144
      
      bit_count -= 12
      return 33
    
    if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
        bit_count -= 13
        return 40
      
      bit_count -= 13
      return 220
    
    if (((bit_buffer >> (bit_count - 13)) & 1) != 1) :
      bit_count -= 13
      return 125
    
    if (((bit_buffer >> (bit_count - 14)) & 1) != 1) :
      if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
        bit_count -= 15
        return 182
      
      bit_count -= 15
      return 187
    
    if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
      bit_count -= 15
      return 218
    
    if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
      bit_count -= 16
      return 41
    
    bit_count -= 16
    return 138
  
  if (((bit_buffer >> (bit_count - 8)) & 1) != 1) :
    if (((bit_buffer >> (bit_count - 9)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 10)) & 1) == 1) :
        bit_count -= 10
        return 193
      
      bit_count -= 10
      return 62
    
    if (((bit_buffer >> (bit_count - 10)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 11)) & 1) == 1) :
        bit_count -= 11
        return 243
      
      bit_count -= 11
      return 207
    
    if (((bit_buffer >> (bit_count - 11)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
        bit_count -= 12
        return 130
      
      bit_count -= 12
      return 27
    
    if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
        bit_count -= 13
        return 196
      
      bit_count -= 13
      return 35
    
    if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
      bit_count -= 13
      return 115
    
    if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
        bit_count -= 15
        return 237
      
      bit_count -= 15
      return 177
    
    if (((bit_buffer >> (bit_count - 15)) & 1) != 1) :
      bit_count -= 15
      return 235
    
    if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
      bit_count -= 16
      return 234
    
    if (((bit_buffer >> (bit_count - 17)) & 1) == 1) :
      bit_count -= 17
      return 149
    
    bit_count -= 17
    return 174
  
  if (((bit_buffer >> (bit_count - 9)) & 1) != 1) :
    bit_count -= 9
    return 129
  
  if (((bit_buffer >> (bit_count - 10)) & 1) != 1) :
    if (((bit_buffer >> (bit_count - 11)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
        bit_count -= 12
        return 9
      
      if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
        bit_count -= 13
        return 226
      
      bit_count -= 13
      return 59
    
    if (((bit_buffer >> (bit_count - 12)) & 1) != 1) :
      bit_count -= 12
      return 216
    
    if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
      bit_count -= 13
      return 236
    
    if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
      bit_count -= 14
      return 110
    
    if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
      bit_count -= 15
      return 229
    
    if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
      bit_count -= 16
      return 93
    
    bit_count -= 16
    return 87
  
  if (((bit_buffer >> (bit_count - 11)) & 1) == 1) :
    if (((bit_buffer >> (bit_count - 12)) & 1) != 1) :
      bit_count -= 12
      return 160
    
    if (((bit_buffer >> (bit_count - 13)) & 1) == 1) :
      bit_count -= 13
      return 95
    
    bit_count -= 13
    return 19
  
  if (((bit_buffer >> (bit_count - 12)) & 1) == 1) :
    bit_count -= 12
    return 230
  
  if (((bit_buffer >> (bit_count - 13)) & 1) != 1) :
    if (((bit_buffer >> (bit_count - 14)) & 1) == 1) :
      if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
        bit_count -= 15
        return 185
      
      bit_count -= 15
      return 92
    
    if (((bit_buffer >> (bit_count - 15)) & 1) != 1) :
      bit_count -= 15
      return 137
    
    if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
      bit_count -= 16
      return 210
    
    bit_count -= 16
    return 43
  
  if (((bit_buffer >> (bit_count - 14)) & 1) != 1) :
    if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
      bit_count -= 15
      return 46
    
    bit_count -= 15
    return 183
  
  if (((bit_buffer >> (bit_count - 15)) & 1) == 1) :
    if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
      bit_count -= 16
      return 101
    
    bit_count -= 16
    return 74
  
  if (((bit_buffer >> (bit_count - 16)) & 1) == 1) :
    bit_count -= 16
    return 53
  
  bit_count -= 16
  return 146



def a(z, x, y):
    k = 0
    i = x << 1
    j = y << 2
    if j < 240 and i < 320 and z[j][i]:
        k |= 0x1
    if j + 1 < 240 and i < 320 and z[j + 1][i]:
        k |= 0x2
    if j + 2 < 240 and i < 320 and z[j + 2][i]:
        k |= 0x4
    if j + 3 < 240 and i < 320 and z[j + 3][i]:
        k |= 0x40
    if j < 240 and i + 1 < 320 and z[j][i + 1]:
        k |= 0x8
    if j + 1 < 240 and i + 1 < 320 and z[j + 1][i + 1]:
        k |= 0x10
    if j + 2 < 240 and i + 1 < 320 and z[j + 2][i + 1]:
        k |= 0x20
    if j + 3 < 240 and i + 1 < 320 and z[j + 3][i + 1]:
        k |= 0x80
    return I[18][k]

I = [0 for i in range(20)]
I[14] = b'\x1b[2J\x1b[1;1H'.decode()
I[15] = b'\n'.decode()
I[16] = b'\x1b['.decode()
I[18] = b'\xe2\xa0\x80\xe2\xa0\x81\xe2\xa0\x82\xe2\xa0\x83\xe2\xa0\x84\xe2\xa0\x85\xe2\xa0\x86\xe2\xa0\x87\xe2\xa0\x88\xe2\xa0\x89\xe2\xa0\x8a\xe2\xa0\x8b\xe2\xa0\x8c\xe2\xa0\x8d\xe2\xa0\x8e\xe2\xa0\x8f\xe2\xa0\x90\xe2\xa0\x91\xe2\xa0\x92\xe2\xa0\x93\xe2\xa0\x94\xe2\xa0\x95\xe2\xa0\x96\xe2\xa0\x97\xe2\xa0\x98\xe2\xa0\x99\xe2\xa0\x9a\xe2\xa0\x9b\xe2\xa0\x9c\xe2\xa0\x9d\xe2\xa0\x9e\xe2\xa0\x9f\xe2\xa0\xa0\xe2\xa0\xa1\xe2\xa0\xa2\xe2\xa0\xa3\xe2\xa0\xa4\xe2\xa0\xa5\xe2\xa0\xa6\xe2\xa0\xa7\xe2\xa0\xa8\xe2\xa0\xa9\xe2\xa0\xaa\xe2\xa0\xab\xe2\xa0\xac\xe2\xa0\xad\xe2\xa0\xae\xe2\xa0\xaf\xe2\xa0\xb0\xe2\xa0\xb1\xe2\xa0\xb2\xe2\xa0\xb3\xe2\xa0\xb4\xe2\xa0\xb5\xe2\xa0\xb6\xe2\xa0\xb7\xe2\xa0\xb8\xe2\xa0\xb9\xe2\xa0\xba\xe2\xa0\xbb\xe2\xa0\xbc\xe2\xa0\xbd\xe2\xa0\xbe\xe2\xa0\xbf\xe2\xa1\x80\xe2\xa1\x81\xe2\xa1\x82\xe2\xa1\x83\xe2\xa1\x84\xe2\xa1\x85\xe2\xa1\x86\xe2\xa1\x87\xe2\xa1\x88\xe2\xa1\x89\xe2\xa1\x8a\xe2\xa1\x8b\xe2\xa1\x8c\xe2\xa1\x8d\xe2\xa1\x8e\xe2\xa1\x8f\xe2\xa1\x90\xe2\xa1\x91\xe2\xa1\x92\xe2\xa1\x93\xe2\xa1\x94\xe2\xa1\x95\xe2\xa1\x96\xe2\xa1\x97\xe2\xa1\x98\xe2\xa1\x99\xe2\xa1\x9a\xe2\xa1\x9b\xe2\xa1\x9c\xe2\xa1\x9d\xe2\xa1\x9e\xe2\xa1\x9f\xe2\xa1\xa0\xe2\xa1\xa1\xe2\xa1\xa2\xe2\xa1\xa3\xe2\xa1\xa4\xe2\xa1\xa5\xe2\xa1\xa6\xe2\xa1\xa7\xe2\xa1\xa8\xe2\xa1\xa9\xe2\xa1\xaa\xe2\xa1\xab\xe2\xa1\xac\xe2\xa1\xad\xe2\xa1\xae\xe2\xa1\xaf\xe2\xa1\xb0\xe2\xa1\xb1\xe2\xa1\xb2\xe2\xa1\xb3\xe2\xa1\xb4\xe2\xa1\xb5\xe2\xa1\xb6\xe2\xa1\xb7\xe2\xa1\xb8\xe2\xa1\xb9\xe2\xa1\xba\xe2\xa1\xbb\xe2\xa1\xbc\xe2\xa1\xbd\xe2\xa1\xbe\xe2\xa1\xbf\xe2\xa2\x80\xe2\xa2\x81\xe2\xa2\x82\xe2\xa2\x83\xe2\xa2\x84\xe2\xa2\x85\xe2\xa2\x86\xe2\xa2\x87\xe2\xa2\x88\xe2\xa2\x89\xe2\xa2\x8a\xe2\xa2\x8b\xe2\xa2\x8c\xe2\xa2\x8d\xe2\xa2\x8e\xe2\xa2\x8f\xe2\xa2\x90\xe2\xa2\x91\xe2\xa2\x92\xe2\xa2\x93\xe2\xa2\x94\xe2\xa2\x95\xe2\xa2\x96\xe2\xa2\x97\xe2\xa2\x98\xe2\xa2\x99\xe2\xa2\x9a\xe2\xa2\x9b\xe2\xa2\x9c\xe2\xa2\x9d\xe2\xa2\x9e\xe2\xa2\x9f\xe2\xa2\xa0\xe2\xa2\xa1\xe2\xa2\xa2\xe2\xa2\xa3\xe2\xa2\xa4\xe2\xa2\xa5\xe2\xa2\xa6\xe2\xa2\xa7\xe2\xa2\xa8\xe2\xa2\xa9\xe2\xa2\xaa\xe2\xa2\xab\xe2\xa2\xac\xe2\xa2\xad\xe2\xa2\xae\xe2\xa2\xaf\xe2\xa2\xb0\xe2\xa2\xb1\xe2\xa2\xb2\xe2\xa2\xb3\xe2\xa2\xb4\xe2\xa2\xb5\xe2\xa2\xb6\xe2\xa2\xb7\xe2\xa2\xb8\xe2\xa2\xb9\xe2\xa2\xba\xe2\xa2\xbb\xe2\xa2\xbc\xe2\xa2\xbd\xe2\xa2\xbe\xe2\xa2\xbf\xe2\xa3\x80\xe2\xa3\x81\xe2\xa3\x82\xe2\xa3\x83\xe2\xa3\x84\xe2\xa3\x85\xe2\xa3\x86\xe2\xa3\x87\xe2\xa3\x88\xe2\xa3\x89\xe2\xa3\x8a\xe2\xa3\x8b\xe2\xa3\x8c\xe2\xa3\x8d\xe2\xa3\x8e\xe2\xa3\x8f\xe2\xa3\x90\xe2\xa3\x91\xe2\xa3\x92\xe2\xa3\x93\xe2\xa3\x94\xe2\xa3\x95\xe2\xa3\x96\xe2\xa3\x97\xe2\xa3\x98\xe2\xa3\x99\xe2\xa3\x9a\xe2\xa3\x9b\xe2\xa3\x9c\xe2\xa3\x9d\xe2\xa3\x9e\xe2\xa3\x9f\xe2\xa3\xa0\xe2\xa3\xa1\xe2\xa3\xa2\xe2\xa3\xa3\xe2\xa3\xa4\xe2\xa3\xa5\xe2\xa3\xa6\xe2\xa3\xa7\xe2\xa3\xa8\xe2\xa3\xa9\xe2\xa3\xaa\xe2\xa3\xab\xe2\xa3\xac\xe2\xa3\xad\xe2\xa3\xae\xe2\xa3\xaf\xe2\xa3\xb0\xe2\xa3\xb1\xe2\xa3\xb2\xe2\xa3\xb3\xe2\xa3\xb4\xe2\xa3\xb5\xe2\xa3\xb6\xe2\xa3\xb7\xe2\xa3\xb8\xe2\xa3\xb9\xe2\xa3\xba\xe2\xa3\xbb\xe2\xa3\xbc\xe2\xa3\xbd\xe2\xa3\xbe\xe2\xa3\xbf'.decode()

I[11] = b'\x1b[%d;%dH'.decode() 
I[12] = b'\x1b[?25l'.decode()
I[13] = b'\x1b[2J\x1b[1;1H'.decode()


print(I[11] % (33, 81), end='')
import sys
sys.stdout.flush()
print(I[12], end='')
print(I[13], end='')

# with open("extracted2","rb") as f:
with open("data2-extract","rb") as f:
    
    stream_data = f.read()


zArr = [[False for _ in range(320)] for _ in range(240)]


def append_number_fast(filename, a,b,c):
    with open(filename, 'a', buffering=1) as f:
        f.write(f"{a} {b} {c}\n")






curr = 0
bit_buffer = 0
bit_count = 0
 


 
frames = 0

while curr < len(stream_data):

  
  iB = (b() & 0xFF) | ((b() & 0xFF) << 8)
  bArr = bytearray(150)
  for i in range(150):
      bArr[i] = b()
  
  
  k = 0
  zArr2 = [[False for _ in range(160)] for _ in range(60)]

  for i7 in range(1200):
    if k >= iB:
        break

    if (bArr[i7 // 8] & (1 << (i7 % 8))) != 0:
        i8 = i7 % 40
        lllllllllIllIII = i7 // 40

        for i9 in range(8):
            iB2 = b()
            for i10 in range(8):
                zArr[(lllllllllIllIII << 3) + i9][(i8 << 3) + i10] = ((iB2 >> (7 - i10)) & 1) != 0

        for i11 in range(2):
            for i12 in range(4):
                zArr2[(lllllllllIllIII << 1) + i11][(i8 << 2) + i12] = True

        k += 1  
  


  sb = []


  if iB > 300:
      sb.append(I[14])
      for i13 in range(60):
          for i14 in range(160):
              sb.append(a(zArr, i14, i13))  # assumed: a(zArr, x, y) returns a char
          if i13 < 59:
              sb.append(I[15])
  else:
      for i15 in range(60):
          i16 = 0
          while i16 < 160:
              if zArr2[i15][i16]:
                  i17 = i16
                  while i16 < 160 and zArr2[i15][i16]:
                      i16 += 1
                  lllllllllIllIII2 = i16 - 1
                  sb2 = []
                  for i18 in range(i17, lllllllllIllIII2 + 1):
                      sb2.append(a(zArr, i18, i15))
                  sb.append(I[16])
                  sb.append(str(i15 + 1))
                  sb.append(';')
                  sb.append(str(i17 + 1))
                  sb.append('H')
                  sb.append(''.join(chr(x) if isinstance(x, int) else x for x in sb2))
              else:
                  i16 += 1
  

  printed = ''.join(chr(x) if isinstance(x, int) else x for x in sb)
  print(printed)
  append_number_fast("curr2.num",curr,bit_buffer,bit_count)
  # print(curr)
  # break