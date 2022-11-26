while True:
    for each_event in pygame.event.get():
        if each_event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
