import schedule
import weather

'''This method contains all the scheduling tasks'''
def grow():
    schedule.every(2).minutes.do(job)
    while True:
        schedule.run_pending()


'''Different branches of the tree can grow using different methods.
To start, I just have a method to get the current weather conditions'''
def job():
    weather.get_weather()
    return


if __name__ == "__main__":
    grow()