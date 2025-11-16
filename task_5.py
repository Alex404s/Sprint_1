class TestCase():

    def __init__(self, steps={}, result='None'):
        self.testcase_steps = steps
        self.testcase_result = result

    def set_step(self, step_number, step_text):
        self.set_step_number = step_number
        self.set_step_text = step_text
        self.testcase_steps[self.set_step_number] = self.set_step_text        

    def delete_step(self, step_number):
        self.delete_step_number = step_number
        del self.testcase_steps[self.delete_step_number]
        

    def set_result(self, result):
        self.set_result = result
        self.testcase_result = self.set_result        

    def get_test_case(self):
        print({'Шаги':self.testcase_steps, 'Ожидаемый результат':self.testcase_result})
         

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case() 
