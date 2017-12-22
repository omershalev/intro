if __name__ == '__main__':

    # Import a module and access a function under this module
    import module_to_import_from
    module_to_import_from.my_function()

    # Create alias to the module name
    import module_to_import_from as m
    m.my_function()

    # Import a specific object from a module
    from module_to_import_from import x
    print x

    # Import all objects under a module
    from module_to_import_from import *
    my_function()
    print x
    print y