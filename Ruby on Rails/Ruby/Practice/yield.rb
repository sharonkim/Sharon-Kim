def execute_block
    yield
end

execute_block { puts 'Hello!'}



def execute_block
    yield 'string', 5
end

execute_block { |string_received, val| puts string_received, val }
