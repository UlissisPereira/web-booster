import queue
from services.log import Log
from services.driver import Driver
from multiprocessing import Process, Queue


class WebProcess:
    number_procs = 20
    procs = []
    tasks = Queue()
    driver = Driver()
    log = Log()
        
    def run(self) -> None:
        
        for i in range(self.number_procs):
            self.tasks.put(i)
        
        for n in range(self.number_procs):
            proc = Process(target=self.read_news, args=(self.tasks, self.number_procs))
            self.procs.append(proc)
            proc.start()
    
    def read_news(self, tasks, count):
        while True:
            try:
                tasks.get_nowait()
                self.driver.run()
            except queue.Empty:
                break
            except AttributeError as e:
                self.log.log_error.error("{} : {}".format(type(e).__name__, e))
                break
            except Exception as e:
                tasks.put(count)
                self.log.log_error.error("{} : {}".format(type(e).__name__, e))
            finally:
                break

        return True
            