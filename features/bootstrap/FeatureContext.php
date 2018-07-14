<?php

include_once(__DIR__ . '/../../php/class-ee.php');
include_once(__DIR__ . '/../../php/utils.php');

use Behat\Behat\Context\Context;
use Behat\Behat\Hook\Scope\AfterFeatureScope;


use Behat\Gherkin\Node\PyStringNode,
	Behat\Gherkin\Node\TableNode;

class FeatureContext implements Context
{
	public $command;
	public $webroot_path;

	/**
	 * @Given ee phar is generated
	 */
	public function eePharIsPresent()
	{
		// Checks if phar already exists, replaces it
		if(file_exists('ee-old.phar')) {
			// Below exec call is required as currenly `ee cli update` is ran with root
			// which updates ee.phar with root privileges.
			exec("sudo rm ee.phar");
			copy('ee-old.phar','ee.phar');
			return 0;
		}
		exec("php -dphar.readonly=0 utils/make-phar.php ee.phar", $output, $return_status);
		if (0 !== $return_status) {
			throw new Exception("Unable to generate phar" . $return_status);
		}

		// Cache generaed phar as it is expensive to generate one
		copy('ee.phar','ee-old.phar');
	}

	/**
	 * @Given :command is installed
	 */
	public function isInstalled($command)
	{
		exec("type " . $command, $output, $return_status);
		if (0 !== $return_status) {
			throw new Exception($command . " is not installed! Exit code is:" . $return_status);
		}
	}

	/**
	 * @When I run :command
	 */
	public function iRun($command)
	{
		$this->command = EE::launch($command, false, true);
	}
	/**
	 * @Then return value should be 0
	 */
	public function returnCodeShouldBe0()
	{
		if ( 0 !== $this->command->return_code ) {
			throw new Exception("Actual return code is not zero: \n" . $this->command);
		}
	}

	/**
	 * @Then /(STDOUT|STDERR) should return exactly/
	 */
	public function stdoutShouldReturnExactly($output_stream, PyStringNode $expected_output)
	{
		$command_output = $output_stream === "STDOUT" ? $this->command->stdout : $this->command->stderr;

		$command_output = str_replace(["\033[1;31m","\033[0m"],'',$command_output);

		$expected_out = isset($expected_output->getStrings()[0]) ? $expected_output->getStrings()[0] : '';
		if ( $expected_out !== trim($command_output)) {
			throw new Exception("Actual output is:\n" . $command_output);
		}
	}

	/**
	 * @Then /(STDOUT|STDERR) should return something like/
	 */
	public function stdoutShouldReturnSomethingLike($output_stream, PyStringNode $expected_output)
	{
		$command_output = $output_stream === "STDOUT" ? $this->command->stdout : $this->command->stderr;

		$expected_out = isset($expected_output->getStrings()[0]) ? $expected_output->getStrings()[0] : '';
		if (strpos($command_output, $expected_out) === false) {
			throw new Exception("Actual output is:\n" . $command_output);
		}
	}

	
	/**
	 * @AfterFeature
	 */
	public static function cleanup(AfterFeatureScope $scope)
	{
		if(file_exists('ee.phar')) {
			unlink('ee.phar');
		}
		if(file_exists('ee-old.phar')) {
			unlink('ee-old.phar');
		}
	}
}
