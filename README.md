# SuperDebugger
Guaranteed to solve 100% of bugs.

# Usage
Simply import the decorator function and wrap any function you'd like to debug.

    from superdebugger import debug

    @debug
    main():
        pass

    if __name__ == '__main__':
        main()
