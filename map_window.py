def map_window(p, w, v):
  
  lv = v[0]
  av = v[1]
  xi = j[0]
  yi = j[1]
  xf = j[2]
  yf = j[3]
  
  m = [0] * 3
  m = m * 3
  m[0][0] = lv/(xf-xi)
  m[0][2] = (1 - xi*lv/(xf-xi))
  m[1][1] = av/(yf-yi)
  m[1][2] = (1 - yi*av/(yf-yi))
  m[2][2] = 1
  
