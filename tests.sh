clear
echo -e	"Testing has started...\n"

echo -e "#################################"
echo -e "#Tests that should be successful#"
echo -e "#################################"
echo -e "#1: python main.py -ip 127.0.0.1"
python main.py -ip 127.0.0.1; echo -e '\n'

echo -e "#2: python main.py -ip list_example"
python main.py -ip list_example; echo -e '\n'

echo -e "###################################"
echo -e "#Tests that should be an exception#"
echo -e "###################################"
echo -e "#1: python main.py"
python main.py; echo -e '\n'

echo -e "#2: python main.py -ip list_exampl"
python main.py -ip list_exampl; echo -e '\n'

echo -e "#3: python main.py -ip 127.0.0.a"
python main.py -ip 127.0.0.a; echo -e '\n'

echo -e "#4: python main.py -ip 127.0.0.1234"
python main.py -ip 127.0.0.1234; echo -e '\n'

echo -e "#5: python main.py -ip"
python main.py -ip

