#include "zombie.h"

/**
 * main - Creates a zombie process
 *
 * Return: 0
 */
int main(void)
{
	pid_t child_pid;
	int i = 0;

	while (i < 5)
	{
		child_pid = fork();
		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(1);
			i++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
/**
 * infinite_while - Runs a while loop infinitely
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
