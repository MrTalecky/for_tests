from Appfollow import UseElements


def test_reg_app(browser):
    reg_main_page = UseElements(browser)
    reg_main_page.go_to_site()
    reg_main_page.click_on_create_account_button()
    reg_main_page.enter_email("talecky@gmail.com")
    reg_main_page.enter_fullname("Ivan QA")
    reg_main_page.enter_company("testCompany_01")
    reg_main_page.choose_position()
    reg_main_page.click_on_submit_button()
    elements = reg_main_page.click_assert_tab()
    assert "Попробуйте бесплатный план" and "Не включено в этот план:" in elements
