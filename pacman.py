def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can a ghost be eaten?
    """
    # Pac-Man can eat a ghost if he has a power pellet active AND he is touching a ghost
    return power_pellet_active and touching_ghost

# Test the function with different combinations of inputs
if __name__ == "__main__":
    # Test case 1: Power pellet active and touching ghost
    print("Test 1: Power pellet active and touching ghost")
    result = eat_ghost(True, True)
    print(f"Result: {result}")
    print(f"Expected: True")
    print()
    
    # Test case 2: Power pellet active but not touching ghost
    print("Test 2: Power pellet active but not touching ghost")
    result = eat_ghost(True, False)
    print(f"Result: {result}")
    print(f"Expected: False")
    print()
    
    # Test case 3: No power pellet but touching ghost
    print("Test 3: No power pellet but touching ghost")
    result = eat_ghost(False, True)
    print(f"Result: {result}")
    print(f"Expected: False")
    print()
    
    # Test case 4: No power pellet and not touching ghost
    print("Test 4: No power pellet and not touching ghost")
    result = eat_ghost(False, False)
    print(f"Result: {result}")
    print(f"Expected: False")
