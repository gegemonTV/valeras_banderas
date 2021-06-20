def to_seconds(hours=0, mins=0, secs=0):
  return hours*60*60+mins*60+secs

def variant(x):
    lastTwoDigits = x % 100
    tens = lastTwoDigits // 10
    if tens == 1:
        return 2
    ones = lastTwoDigits % 10
    if ones == 1:
        return 0
    if ones >= 2 and ones <= 4:
        return 1
    return 2

def from_seconds(seconds=0):
  hours = seconds // 3600
  seconds = seconds - (hours * 3600)
  minutes = seconds // 60
  seconds = seconds - (minutes * 60)
  str_sec = ["cекунда", "секунды", "секунд"][variant(seconds)]
  str_min = ["минута", "минуты", "минут"][variant(minutes)]
  str_hours = ["час", "часа", "часов"][variant(hours)]
  print(f"{hours} {str_hours} {minutes} {str_min} {seconds} {str_sec}")