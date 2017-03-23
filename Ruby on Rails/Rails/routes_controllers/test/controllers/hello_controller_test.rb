require 'test_helper'

class HelloControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get hello_index_url
    assert_response :success
  end

  test "should get dojo" do
    get hello_dojo_url
    assert_response :success
  end

  test "should get say_hello" do
    get hello_say_hello_url
    assert_response :success
  end

  test "should get joe" do
    get hello_joe_url
    assert_response :success
  end

  test "should get michael" do
    get hello_michael_url
    assert_response :success
  end

  test "should get times" do
    get hello_times_url
    assert_response :success
  end

  test "should get restart" do
    get hello_restart_url
    assert_response :success
  end

end
