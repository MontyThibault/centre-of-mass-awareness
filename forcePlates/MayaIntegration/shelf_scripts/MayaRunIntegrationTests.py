from utils.safe_module_wrapper import safe_module_wrapper


@safe_module_wrapper
def main():

	from tests_integration.main import main
	main()


if __name__ == '__main__':

	main()

