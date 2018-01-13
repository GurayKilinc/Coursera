"""
Cookie Clicker Simulator
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self.total_cookies = 0.0
        self.current_cookies = 0.0
        self.current_time = 0.0
        self.current_cps = 1.0
        self.history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        print('\n')
        print(self.current_time)
        print(self.current_cookies)
        print(self.current_cps)
        print(self.total_cookies)
        return ""
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self.current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self.current_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self.current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self.history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        wait_time = 0
        if self.current_cookies < cookies:
            wait_time = math.ceil((cookies - self.current_cookies) / self.current_cps)
        return float(wait_time)
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0:
            self.total_cookies += self.get_cps() * time
            self.current_cookies += self.get_cps() * time
            self.current_time += time
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self.current_cookies >= cost:
            self.current_cookies -= cost
            self.current_cps += additional_cps
            self.history.append( (self.get_time(), item_name, cost, self.total_cookies) )
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    new_build_info = build_info.clone()
    new_state = ClickerState()
    while new_state.get_time() <= duration:
        next_update = strategy(new_state.get_cookies(), new_state.get_cps(), new_state.get_history(), 
                               duration - new_state.get_time(), new_build_info)
        if next_update == None:
            new_state.wait(duration - new_state.get_time())
            return new_state
        elif new_build_info.get_cost(next_update) > new_state.get_cookies() + (new_state.get_cps() * (duration - new_state.get_time())):
            new_state.wait(duration - new_state.get_time())
            return new_state
        else:
            wait_time = new_state.time_until(new_build_info.get_cost(next_update))
            new_state.wait(wait_time)
            new_state.buy_item(next_update, new_build_info.get_cost(next_update), new_build_info.get_cps(next_update))
            new_build_info.update_item(next_update)
    return new_state




def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    # get available items from build_info
    available_items = build_info.build_items()

    # build a dictionary for the items and costs
    my_dictionary = {}
    for each_item in available_items:
        my_dictionary[each_item] = my_dictionary.get(each_item, build_info.get_cost(each_item))

    # build a sorted list based on the cost
    temp_list = sorted((value, key) for (key, value) in my_dictionary.items())

    # get the current cheapest item
    next_item = temp_list[0][1]

    # check if time left is enough to buy this next_item, if not, return None
    if cps * time_left + cookies < build_info.get_cost(next_item):
        return None

    # otherwise, return this item
    return next_item

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    # get available items from build_info
    available_items = build_info.build_items()

    # build a dictionary for the items and costs
    my_dictionary = {}
    for each_item in available_items:
        my_dictionary[each_item] = my_dictionary.get(each_item, build_info.get_cost(each_item))

    # build a sorted list based on the cost
    temp_list = sorted(((value, key) for (key, value) in my_dictionary.items()), reverse=True)

    # for each item in the list, pick the one with highest cost, check if time left is enough to buy this next_item,
    # if not, try next one, until found one and break
    while temp_list:  # do it until no choice
        next_item = temp_list[0][1]
        if cps * time_left + cookies >= build_info.get_cost(next_item):
            # time is enough, break
            return next_item
        # otherwise, move to the next
        temp_list = temp_list[1:]

    # otherwise, return None
    return None

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    # get available items from build_info
    available_items = build_info.build_items()

    # build a dictionary for the items and cost/cps
    my_dictionary = {}
    for each_item in available_items:
        my_dictionary[each_item] = my_dictionary.get(each_item,
                                                     build_info.get_cost(each_item) / build_info.get_cps(each_item))

    # build a sorted list based on cost/cps
    temp_list = sorted((value, key) for (key, value) in my_dictionary.items())

    # for each item in the list, pick the one with lowest cost/cps, check if time left is enough to buy this next_item,
    # if not, try next one, until found one and break
    while temp_list:  # do it until no choice
        next_item = temp_list[0][1]
        if cps * time_left + cookies >= build_info.get_cost(next_item):
            # time is enough, break
            return next_item
        # otherwise, move to the next
        temp_list = temp_list[1:]

    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
run()
    

