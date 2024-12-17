from bluedot import BlueDot

bd = BlueDot(rows=2, cols=2, text='HELLO')
bd[0,0].color = 'green'
bd[0,1].color = 'red'
bd[0,1].square = True
bd[0,1].text = 'RED'

bd.wait_for_press()
print('Yeah')
