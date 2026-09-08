import ollama
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def calculator(x, y, operation):
    x=float(x)
    y=float(y)
    if operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y
    elif operation == 'multiply':
        return x * y
    elif operation == 'divide':
        if y == 0:
            return "Error: cannot divide by zero"
        return x / y
    
tools = [
    {
        'type': 'function',
        'function': {
            'name': 'calculator',
            'description': 'Performs arithmetic: add, subtract, multiply, divide',
            'parameters': {
                'type': 'object',
                'properties': {
                    'x': {'type': 'number', 'description': 'first number'},
                    'y': {'type': 'number', 'description': 'second number'},
                    'operation': {
                        'type': 'string',
                        'description': 'add, subtract, multiply, or divide'
                    }
                },
                'required': ['x', 'y', 'operation']
            }
        }
    },
    {
    'type': 'function',
    'function': {
        'name': 'get_current_time',
        'description': 'Returns the current date and time',
        'parameters': {'type': 'object', 'properties': {}, 'required': []}
    }
}
]
while True:
    inpot_user=input('Ask me anything (calc or chat, "exit" to quit): ')

    if inpot_user.lower()=='exit':
        break
    messages=[{'role': 'user', 'content': inpot_user}]

    response = ollama.chat(
        model='llama3.2',
        messages=messages,
        tools=tools
    )
    if response['message'].tool_calls:
        tool_name=response['message'].tool_calls[0].function.name
        arguments=response['message'].tool_calls[0].function.arguments
        print(f"[AGENT] Tool chosen: {tool_name}")
        try:
            if tool_name == 'calculator':
                result= calculator(**arguments)
                print(f"[AGENT] Arguments: {arguments}")
                print(f"[AGENT] Result: {result}")
            elif tool_name == 'get_current_time':
                result = get_current_time()
                print(f"[AGENT] Result: {result}")
            else:
                result =f'Error: unknown tool {tool_name}'
                print("[AGENT] No tool needed, answering directly")
        except Exception as e:
            result=f"Error: {e}"

        messages.append(response['message'])
        messages.append({'role': 'tool', 'content': str(result)})
        final = ollama.chat(model='llama3.2', messages=messages)
        print(final['message']['content'])

    else:
        print(response['message']['content'])

    


